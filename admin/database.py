import os
from mongoengine import connect
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# mongodb
def to_dict(document):
  tmp = document.to_mongo().to_dict()
  if '_id' in tmp:
    tmp['_id'] = str(document.id)
  return tmp

def db_connect():
  connect(
    db='chatsv2',
    username='',
    password='',
    host='localhost',
    port=27017
  )

# relational db
load_dotenv()
db_version = os.getenv('DB_VERSION')
engine = create_engine(f"sqlite:///db/fifa25v{db_version}.db")  # Cambia a tu DB
Session = sessionmaker(bind=engine)