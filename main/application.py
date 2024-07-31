# !/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from flask_session import Session
from .blueprints import register
from .helpers import scripts, styles
from .constants import CONSTANTS
from .blueprints import register
from .middlewares import not_found

APP = Flask(
  __name__,
  static_folder='../static',
  static_url_path='/'
)
APP.config['SECRET_KEY'] = 'your_secret_key'
APP.config['SESSION_TYPE'] = 'filesystem'
APP.config['SESSION_PERMANENT'] = False
APP.config['SESSION_USE_SIGNER'] = True
APP.config['SESSION_KEY_PREFIX'] = 'session:'
Session(APP)

# filters/helpers in templates
@APP.context_processor
def utility_processor():
  return dict(
    styles=styles,
    scripts=scripts,
    constants=CONSTANTS,
  )

register(APP)
APP.register_error_handler(404, not_found)
