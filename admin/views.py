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
def admin():
  locals = {}
  locals['title'] = 'Admin'
  locals['csss'] = []
  locals['jss'] = ['assets/js/app']
  return render_template('admin.html', locals = locals)