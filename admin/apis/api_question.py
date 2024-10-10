#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os
import traceback
from dotenv import load_dotenv
from flask import Blueprint, request
from langchain_openai import ChatOpenAI
from sqlalchemy import text
from admin.database import engine
from datetime import datetime

api = Blueprint('api-question', __name__)

@api.route('/api/v1/question', methods=['POST'])
def ask():
  try:
    # from data
    data = request.get_json()
    question = data.get('question')  # Extraer la pregunta
    conversation_id = data.get('conversation_id')
    # ask to chatgpt
    db_schema = ''
    base_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(base_dir, '../../db/schema.sql'), 'r') as file:
      db_schema = file.read()
    db_inserts = ''
    with open(os.path.join(base_dir, '../../db/inserts.sql'), 'r') as file:
      db_inserts = file.read()
    db_schema = db_schema + '\n\n en base al esquema anterior, y considerandos los siguientes datos maestros: \n ' + db_inserts + ' \nentonces, cual sería la consulta sql para la siguiente pregunta: \n'
    input_message = f"{db_schema}\n{question}"
    input_message = input_message + '\n\n' + 'en caso de que un join haya dos columnas con el mismo nombre, usar un AS para renombrarlas, ejemplo players.id,players.name, nations.id, nations.name renombrar como players.id AS player_id,players.name AS player_name, nations.id AS nation_id, nations.name AS nation_name'
    # return input_message
    ## OpenAI
    '''
    load_dotenv()
    os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.5)
    ## generate query
    chatgpt_response = llm.invoke(input_message)
    query = chatgpt_response.content
    '''
    query = """
      SELECT players.name AS player_name, nations.name AS nation_name 
      FROM players 
      JOIN nations ON players.nation_id = nations.id 
      WHERE players.sex_id = 1 LIMIT 100;
    """
    # do query to relational db
    response_data = {}
    columns = []
    result_set = []
    columns = set()
    with engine.connect() as connection:
      result = connection.execute(text(query))
      # result set
      result_set = result.mappings().all()
      for dictionary in result_set:
        columns.update(dictionary.keys())
      columns = list(columns)
    now = datetime.now()
    response_data['result_set'] = [dict(row) for row in result_set],
    response_data['columns'] = columns
    response_data['created_at'] = now.strftime("%Y-%m-%d %H:%M:%S")
    response_data['query'] = query
    
    return json.dumps(response_data)
  except Exception as e:
    traceback.print_exc()
    error_message = "Error desconocido: {}".format(str(e))
    return json.dumps({"error": error_message}), 500
