import datetime
from mongoengine import Document, StringField, DateTimeField, ListField, ObjectIdField
from bson import ObjectId

class User(Document):
  id = ObjectIdField(primary_key=True, default=ObjectId)
  username = StringField()
  password = StringField()
  email = StringField()
  image_url = StringField()
  reset_key = StringField()
  activation_key = StringField()
  status = StringField(default='pending')
  created = DateTimeField(default=datetime.datetime.utcnow)
  updated = DateTimeField(default=None, onupdate=datetime.datetime.utcnow)
  access = ListField(DateTimeField())
  # metadata
  meta = {
    'collection': 'users'  # Nombre de la colección a la que deseas mapear
  }

  @classmethod
  def from_map(cls, map):
    return cls(
      id=ObjectId(map.get('_id')) if map.get('_id') else None,
      username=map['username'],
      password=map['password'],
      email=map['email'],
      image_url=map['image_url'],
      reset_key=map['reset_key'],
      activation_key=map['activation_key'],
      pending=map['pending'],
      created=datetime.fromisoformat(map['created']),
      updated=datetime.fromisoformat(map['updated']),
      # access=[map.get('tracks', [])]
    )

  def to_map(self):
    map_data = {
      '_id': str(self.id),
      'username': self.username,
      'password': self.password,
      'email': self.email,
      'image_url': self.image_url,
      'reset_key': self.reset_key,
      'pending': self.pending,
      'created': self.created.isoformat(),
      'updated': '' if self.updated == None else self.updated.isoformat(),
      # 'access': [track.to_map() for track in self.tracks],  # Sin almacenar como una lista
    }
    return map_data
