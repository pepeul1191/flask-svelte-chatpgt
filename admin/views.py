#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from flask import Blueprint, render_template

view = Blueprint('acces-view', __name__, template_folder='./templates')

@view.route('/admin', methods=['GET'])
def admin():
  locals = {}
  locals['title'] = 'Admin'
  locals['csss'] = []
  locals['jss'] = ['assets/js/app']
  return render_template('admin.html', locals = locals)