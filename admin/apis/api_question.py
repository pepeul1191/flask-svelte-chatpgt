#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import traceback
from bson import ObjectId
from datetime import datetime
from admin.database import db_connect
from flask import Blueprint, request
from admin.models.message import Message 
from admin.helpers.chat_helper import openai_answer

api = Blueprint('api-question', __name__)

@api.route('/api/v1/question', methods=['POST'])
def ask():
  try:
    # from data
    data = request.get_json()
    question = data.get('question')  # Extraer la pregunta
    conversation_id = data.get('conversation_id')
    conversation_name = data.get('conversation_name')
    user_id = '6707611a42e497a5badacb4b'
    # ask to chatgpt - helper
    ai_answer = openai_answer(question)
    if ai_answer['status'] == 'success':
      answer = ai_answer['data']
      db_connect()
      message = Message(
        id = ObjectId(),
        question = question,
        answer = answer,
        error = False,
        created = datetime.now()
      )
      message.save()
      # add message to conversation if conversation not exist, else, create conversation and add message

      # response_data['created_at'] = now.strftime("%Y-%m-%d %H:%M:%S")
      return json.dumps(answer.to_map())
    else:
      return json.dumps(ai_answer['message']), 500
  except Exception as e:
    traceback.print_exc()
    error_message = "Error desconocido: {}".format(str(e))
    return json.dumps({"error": error_message}), 500
