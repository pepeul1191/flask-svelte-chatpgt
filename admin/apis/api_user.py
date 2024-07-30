#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os
import traceback
from flask import Blueprint, request
from admin.database import db_connect
from mongoengine import DoesNotExist
from datetime import datetime
from bson.objectid import ObjectId
from admin.models.user import User
from admin.helpers.admin_helper import generate_random_string
from mongoengine import ValidationError, Q
from main.constants import CONSTANTS

api = Blueprint('api-user', __name__)

@api.route('/user/validate', methods=['POST'])
def validate():
  try:
    data = request.get_json()
    user = data.get('user')
    password = data.get('password')
    print(user)
    print(password)
    return ':)'
  except Exception as e:
    traceback.print_exc()
    error_message = "Error desconocido: {}".format(str(e))
    return json.dumps({"error": error_message}), 500
  
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
      print(CONSTANTS)
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