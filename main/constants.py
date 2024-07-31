# !/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from dotenv import load_dotenv

load_dotenv()
ENV = os.getenv('ENV')

if ENV == 'local':
  CONSTANTS = {
    'base_url': 'http://localhost:5000/',
    'static_url': 'http://localhost:5000/',
  }
  SECRET_KEY = 'my_secret_key'
elif ENV == 'ulima':
  CONSTANTS = {
    'base_url': 'http://ulima.edu.pe/',
    'static_url': 'http://localhost:5000/',
  }
  SECRET_KEY = 'my_secret_key'
else:
  CONSTANTS = {
    'base_url': 'http://localhost:5000/',
    'static_url': 'http://localhost:5000/',
    'session': True,
  }
  SECRET_KEY = 'my_secret_key'