#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import traceback
from flask import Blueprint
from admin.database import db_connect
from mongoengine import DoesNotExist
from bson.objectid import ObjectId
from admin.models.conversation import Conversation

api = Blueprint('api-conversation', __name__)
  
@api.route('/api/v1/conversations', methods=['GET'])
def get_user():
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