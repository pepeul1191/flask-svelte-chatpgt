#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os
import traceback
import jwt
from datetime import datetime, timedelta
from flask import Blueprint, request, jsonify, make_response, session
from admin.database import db_connect
from mongoengine import DoesNotExist
from bson.objectid import ObjectId
from admin.models.user import User
from admin.helpers.admin_helper import generate_random_string
from mongoengine import ValidationError, Q
from main.constants import CONSTANTS, SECRET_KEY
from main.middlewares import session_true

api = Blueprint('api-user', __name__)

@api.route('/user/validate', methods=['POST'])
def validate():
  try:
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    query = Q(username=username) & Q(password=password)
    db_connect()
    user = User.objects(query).first()
    if user == None:
      return 'Usuario y/o contraseña inválidos', 500
    else:
      # JWT
      payload = {
        'id': str(user.id),
        'username': user.username,
        'image_url': user.image_url,
        'email': user.email,
        'exp': datetime.utcnow() + timedelta(minutes=40)
      }
      token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
      response = make_response({
        'message': 'Login correcto', 
        'url': '/admin' if user == 'admin' else '/'
      })
      response.set_cookie('authToken', token, httponly=True, secure=True)
      # session
      session['status'] = True
      session['jwt'] = payload
      return response
  except Exception as e:
    traceback.print_exc()
    error_message = "Error desconocido: {}".format(str(e))
    return json.dumps({"error": error_message}), 500
  
@session_true
@api.route('/user/token', methods=['GET'])
def user_token():
  token = request.cookies.get('authToken')
  if not token:
    return jsonify({'message': 'Token is missing!'}), 403
  try:
    decoded_payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
    return jsonify(decoded_payload)
  except jwt.ExpiredSignatureError:
    return jsonify({'message': 'Token has expired!'}), 403
  except jwt.InvalidTokenError:
    return jsonify({'message': 'Invalid token!'}), 403
  
@session_true
@api.route('/user/session', methods=['GET'])
def user_session():
  if not session:
    return 'No hay sessión creada', 403
  else:
    return jsonify(session), 200
  
@api.route('/user/sign-out', methods=['GET'])
def user_signout():
  session.clear()
  response = make_response(jsonify({'message': 'Logged out successfully!'}))
  response.set_cookie('authToken', '', expires=0, httponly=True, secure=True, samesite='Strict')
  return response
  
@api.route('/user/create', methods=['POST'])
def create():
  try:
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    # validte
    query = Q(username=username) | Q(email=email)
    db_connect()
    user = User.objects(query).first()
    if user == None:
      user_doc = User(
        username = username,
        password = password,
        email = email,
        image_url = 'default.png',
        reset_key = '',
        activation_key = generate_random_string(20),
        updated = None,
        access = [],
      )
      user_doc.save()
      # print(CONSTANTS)
      activation_url = "{}user/activate?_id={}&activation-key={}".format(
        CONSTANTS['base_url'],
        str(user_doc.id),
        user_doc.activation_key,
      )
      print(activation_url)
      # TODO: send meail with activation_url
      return 'Se ha enviado un correo para activar su cuenta', 200
    else:
      return 'Usuario y/o correo en uso', 500
  except Exception as e:
    traceback.print_exc()
    error_message = "Error desconocido: {}".format(str(e))
    return json.dumps({"error": error_message}), 500
  
@api.route('/user/reset-password', methods=['POST'])
def reset_password():
  try:
    data = request.get_json()
    email = data.get('email')
    # validte
    query = Q(email=email)
    db_connect()
    user = User.objects(query).first()
    if user == None:
      return 'Correo no registrado a un usuario', 500
    else:
      user.reset_key = generate_random_string(20)
      user.save()
      reset_url = "{}user/reset-password?_id={}&reset-key={}".format(
        CONSTANTS['base_url'],
        str(user.id),
        user.reset_key,
      )
      print(reset_url)
      # TODO: send meail with reset_url
      return 'Se ha enviado un correo para cambiar su contraseña', 200
  except Exception as e:
    traceback.print_exc()
    error_message = "Error desconocido: {}".format(str(e))
    return json.dumps({"error": error_message}), 500