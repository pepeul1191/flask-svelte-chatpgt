#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import traceback
from dotenv import load_dotenv
from bson import ObjectId
from langchain_openai import ChatOpenAI
from sqlalchemy import text
from admin.database import engine
from admin.models.answer import Answer

def openai_answer(question):
  try:
    # ask to chatgpt
    load_dotenv()
    db_schema = ''
    db_version = os.getenv('DB_VERSION')
    base_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(base_dir, f"../../db/schema_v{db_version}.sql"), 'r') as file:
      db_schema = file.read()
    db_inserts = ''
    with open(os.path.join(base_dir, f"../../db/inserts_v{db_version}.sql"), 'r') as file:
      db_inserts = file.read()
    db_schema = db_schema + '\n\n en base al esquema anterior, y considerandos los siguientes datos maestros: \n ' + db_inserts + ' \nentonces, cual sería la consulta sql para la siguiente pregunta: \n'
    input_message = f"{db_schema}\n{question}"
    input_message = input_message + '\n\n' + 'en caso de que un join haya dos columnas con el mismo nombre, usar un AS para renombrarlas, ejemplo players.id,players.name, nations.id, nations.name renombrar como players.id AS player_id,players.name AS player_name, nations.id AS nation_id, nations.name AS nation_name'
    print(db_schema)
    # exit()
    # return input_message
    if os.getenv('OPENAI_API') == 'true':
      ## OpenAI
      os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
      llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.5)
      ## generate query
      chatgpt_response = llm.invoke(input_message)
      query = chatgpt_response.content
    else:
      ## demo query
      query = """SELECT players.name AS player_name, nations.name AS nation_name 
        FROM players 
        JOIN nations ON players.nation_id = nations.id 
        WHERE players.sex_id = 1 LIMIT 5;"""
    # do query to relational db
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
    answer = Answer(
      id = ObjectId(),
      result_set = [dict(row) for row in result_set],
      columns = columns,
      query = query
    )
    return {'status': 'success', 'data': answer}
  except Exception as e:
    traceback.print_exc()
    error_message = "Error desconocido: {}".format(str(e))
    return {'status': 'error', 'message': error_message}
