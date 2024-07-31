#!/usr/bin/env python
# -*- coding: utf-8 -*-
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from functools import wraps
from flask import session, redirect, request
from .constants import CONSTANTS

# una ruta de errorhandler
def not_found(e):
  # print(request.url)
  if request.method == 'GET':
    extensions_to_check = ['.css', '.js', '.woff', 'png', ]
    if any(ext in request.url for ext in extensions_to_check):
      return 'Recurso no encontrado', 404
    else:
      return redirect('/error/access/404')
  else:
    error = {
      'tipo_mensaje': 'error',
      'mensaje': [
        'Recurso no disponible',
        'Error 404'
      ],
    }
    return json.dumps(error), 404
  
def session_false(fn):
  @wraps(fn)
  def _session_false(*args, **kwargs):
    # si la session es activaa, vamos a '/accesos/'
    if CONSTANTS['session']:
      if session.get('status') is not None:
        if session.get('status'):
          return redirect('/')
      return fn(*args, **kwargs)
    else:
      return fn(*args, **kwargs)
  return _session_false

def session_true(fn):
  @wraps(fn)
  def _session_true(*args, **kwargs):
    # si la session es activaa, vamos a '/accesos/'
    if CONSTANTS['session']:
      if session.get('status') is not None:
        if not session.get('status'):
          return redirect('/error/access/505')
        else:
          return redirect('/error/access/505')
      return fn(*args, **kwargs)
    return _session_true