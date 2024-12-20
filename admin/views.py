#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from flask import Blueprint, render_template
from main.middlewares import session_false

view = Blueprint('acces-view', __name__, template_folder='./templates')

@view.route('/login', methods=['GET'])
@view.route('/sign-up', methods=['GET'])
@view.route('/reset-password', methods=['GET'])
@session_false
def index():
  locals = {}
  locals['title'] = 'Login'
  locals['csss'] = ['dist/access']
  locals['jss'] = ['dist/access']
  return render_template('access.html', locals = locals)

@view.route('/admin', methods=['GET'])
@view.route('/conversations', methods=['GET'])
@view.route('/admin', methods=['GET'])
def admin():
  locals = {}
  locals['title'] = 'Admin'
  locals['csss'] = ['dist/app']
  locals['jss'] = ['dist/app']
  return render_template('admin.html', locals = locals)

@view.route('/conversations/<string:conversation_id>', methods=['GET'])
def conversation_detail(conversation_id):
  locals = {}
  locals['title'] = 'Admin'
  locals['csss'] = ['dist/app']
  locals['jss'] = ['dist/app']
  return render_template('admin.html', locals = locals)