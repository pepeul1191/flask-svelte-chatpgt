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

DB_VERSION = os.getenv('DB_VERSION')

if DB_VERSION == '1':
  DB = {
    'url': 'sqlite:///db/fifa25v1.db',
    'schema': '../../db/schema_v1.sql',
    'inserts': '../../db/inserts_v1.sql',
  }
elif DB_VERSION == '2':
  DB = {
    'url': 'sqlite:///db/fifa25v2.db',
    'schema': '../../db/schema_v2.sql',
    'inserts': '../../db/inserts_v2.sql',
  }
else:
  DB = {
    'url': 'sqlite:///db/fifa25v3.db',
    'schema': '../../db/schema_v3.sql',
    'inserts': '../../db/inserts_v3.sql',
  }