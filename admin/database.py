from mongoengine import connect
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

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
engine = create_engine('sqlite:///db/app.db')  # Cambia a tu DB
Session = sessionmaker(bind=engine)