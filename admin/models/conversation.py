from bson import ObjectId
from mongoengine import DateTimeField, ObjectIdField, StringField, ListField, Document
from datetime import datetime

class Conversation(Document):
  id = ObjectIdField(primary_key=True) 
  name = StringField()
  messages = ListField(ObjectIdField())
  created = DateTimeField(default=datetime.utcnow)
  updated = DateTimeField(default=datetime.utcnow)
  user_id = ObjectIdField() 
  meta = {
    'collection': 'conversations'  # Nombre de la colección a la que deseas mapear
  }

  @classmethod
  def from_map(cls, data):
    return cls(
      id=data.get('id', ObjectId()),
      name=data.get('name'),
      messages=data.get('messages', []),
      created=data.get('created', datetime.utcnow()),
      updated=data.get('updated', datetime.utcnow()),
      user_id=data.get('user_id')
    )

  def to_map(self):
    return {
      'id': str(self.id),
      'name': self.name,
      'messages': self.messages,
      'created': self.created.isoformat(),
      'updated': self.updated.isoformat(),
      'user_id': str(self.user_id) if self.user_id else None
    }

  def __str__(self):
    return (f"Conversation(id={self.id}, name='{self.name}', "
    f"messages={self.messages}, created={self.created.isoformat()}, "
    f"updated={self.updated.isoformat()}, user_id={self.user_id})")