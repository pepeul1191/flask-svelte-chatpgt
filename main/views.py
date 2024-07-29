#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Blueprint, render_template

view = Blueprint('demo-app-index', __name__)

@view.route('/contact', methods=['GET'])
@view.route('/about', methods=['GET'])
@view.route('/', methods=['GET'])
def home():
  locals = {}
  locals['title'] = 'Bienvenido'
  # locals['csss'] = ['dist/bootstrap.min', 'dist/web.min', ]
  # locals['jss'] = ['dist/web.min']
  return render_template('home.html', locals = locals)

@view.route('/login', methods=['GET'])
@view.route('/sign-in', methods=['GET'])
@view.route('/reset-password', methods=['GET'])
def index():
  locals = {}
  locals['title'] = 'Login'
  locals['csss'] = ['dist/login']
  locals['jss'] = ['dist/login']
  return render_template('access.html', locals = locals)

@view.route('/error/access/<code>', methods=['GET'])
def error_access(code):
  # lang = session_language(session)
  # locals_dic = { }
  locals = {}
  locals['title'] = 'Recurso no encontrado'
  locals['code'] = code
  return render_template('error.html', locals=locals)
  # return 'Recurso no encontrado', code
