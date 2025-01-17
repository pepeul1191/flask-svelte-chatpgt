#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import traceback
import os
from dotenv import load_dotenv
from bson import ObjectId
from datetime import datetime
from admin.database import db_connect
from flask import Blueprint, request
from admin.models.conversation import Conversation
from admin.models.message import Message 
from admin.helpers.chat_helper import openai_answer

api = Blueprint('api-question', __name__)

@api.route('/api/v1/questions', methods=['POST'])
def ask():
  try:
    # from data
    data = request.get_json()
    question = data.get('question')  # Extraer la pregunta
    conversation_id = ObjectId(data.get('conversation')['_id'])
    name = data.get('conversation')['name']
    user_id = '6707611a42e497a5badacb4b'
    # ask to chatgpt - helper
    ai_answer = openai_answer(question)
    if ai_answer['status'] == 'success':
      answer = ai_answer['data']
      db_connect()
      message_id = ObjectId()
      load_dotenv()
      message = Message(
        id = message_id,
        question = question,
        answer = answer,
        error = False,
        created_at = datetime.now(),
        db_version = os.getenv('DB_VERSION')
      )
      message.save()
      # add message to conversation if conversation not exist, else, create conversation and add message
      conversation = Conversation.objects(id=conversation_id).first()
      if conversation:
        conversation.name = name
        conversation.messages.append(message_id)
        conversation.updated_at = datetime.utcnow()
        conversation.save()
      else:
        conversation = Conversation(
          id=conversation_id,
          name=name,
          messages=[message_id],
          user_id=user_id
        )
        conversation.save()  # Guarda la nueva conversación
      return json.dumps(message.to_map())
    else:
      return json.dumps(ai_answer['message']), 500
  except Exception as e:
    traceback.print_exc()
    error_message = "Error desconocido: {}".format(str(e))
    return json.dumps({"error": error_message}), 500
