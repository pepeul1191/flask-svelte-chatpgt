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
from admin.models.picture import Picture
from admin.models.track import Track
from admin.models.trip import Trip

api = Blueprint('api-question', __name__)

@api.route('/api/v1/question', methods=['POST'])
def ask():
  try:
    data = request.get_json()
    question = data.get('question')  # Extraer la pregunta
    conversation_id = data.get('conversation_id')
    print(question)
    print(conversation_id)
    return 'XD'
  except Exception as e:
    traceback.print_exc()
    error_message = "Error desconocido: {}".format(str(e))
    return json.dumps({"error": error_message}), 500
