#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, session

view = Blueprint('demo-app-index', __name__)

@view.route('/profile', methods=['GET'])
@view.route('/contact', methods=['GET'])
@view.route('/about', methods=['GET'])
@view.route('/', methods=['GET'])
def home():
  locals = {}
  locals['title'] = 'Bienvenido'
  styles = ['dist/web']
  scripts = ['dist/web']
  if session.get('status') is not None:
    if session.get('status'):
      styles = ['dist/app']
      scripts = ['dist/app']
  locals['csss'] = styles
  locals['jss'] = scripts
  return render_template('web.html', locals = locals)

@view.route('/error/access/<code>', methods=['GET'])
def error_access(code):
  # lang = session_language(session)
  # locals_dic = { }
  locals = {}
  locals['title'] = 'Recurso no encontrado'
  locals['code'] = code
  return render_template('error.html', locals=locals), code
  # return 'Recurso no encontrado', code
