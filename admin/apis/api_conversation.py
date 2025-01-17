#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import traceback
from flask import Blueprint, request
from datetime import datetime
from admin.database import db_connect
from mongoengine import DoesNotExist
from bson.objectid import ObjectId
from admin.models.conversation import Conversation

api = Blueprint('api-conversation', __name__)
  
@api.route('/api/v1/conversations', methods=['GET'])
def fetch_user_converstion():
  try:
    db_connect()
    user_id = ObjectId('6707611a42e497a5badacb4b')
    docs = Conversation.user_conversations(user_id)
    return json.dumps(docs), 200
  except DoesNotExist:
    return json.dumps({"error": "Document not found"}), 404
  except Exception as e:
    traceback.print_exc()
    return json.dumps({"error": str(e)}), 400
  
@api.route('/api/v1/conversations/<conversation_id>', methods=['GET'])
def fetch_converstion_messages(conversation_id):
  try:
    db_connect()
    doc = Conversation.conversation_messages(ObjectId(conversation_id))
    if doc == None:
      return json.dumps({"error": "Document not found"}), 404
    else: 
      return json.dumps(doc), 200
  except DoesNotExist:
    return json.dumps({"error": "Document not found"}), 404
  except Exception as e:
    traceback.print_exc()
    return json.dumps({"error": str(e)}), 400
  
@api.route('/api/v1/conversations/<conversation_id>', methods=['POST'])
def update_name(conversation_id):
  try:
    db_connect()
    conversation = Conversation.objects(id=ObjectId(conversation_id)).first()
    if conversation == None:
      return json.dumps({"error": "Document not found"}), 404
    else: 
      data = request.get_json()
      conversation.name = data['name']
      conversation.updated_at = datetime.utcnow()
      conversation.save() 
      return 'ok', 200
  except DoesNotExist:
    return json.dumps({"error": "Document not found"}), 404
  except Exception as e:
    traceback.print_exc()
    return json.dumps({"error": str(e)}), 400