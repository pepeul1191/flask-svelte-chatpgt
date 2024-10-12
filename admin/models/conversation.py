from bson import ObjectId
from mongoengine import DateTimeField, ObjectIdField, StringField, ListField, Document
from datetime import datetime

class Conversation(Document):
  id = ObjectIdField(primary_key=True) 
  name = StringField()
  messages = ListField(ObjectIdField())
  created_at = DateTimeField(default=datetime.utcnow)
  updated_at = DateTimeField(default=datetime.utcnow)
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
      created_at=data.get('created_at', datetime.utcnow()),
      updated_at=data.get('updated_at', datetime.utcnow()),
      user_id=data.get('user_id')
    )

  def to_map(self):
    return {
      'id': str(self.id),
      'name': self.name,
      'messages': self.messages,
      'created_at': self.created_at.isoformat(),
      'updated_at': self.updated_at.isoformat(),
      'user_id': str(self.user_id) if self.user_id else None
    }

  def __str__(self):
    return (f"Conversation(id={self.id}, name='{self.name}', "
    f"messages={self.messages}, created_at={self.created_at.isoformat()}, "
    f"updated_at={self.updated_at.isoformat()}, user_id={self.user_id})")
  
  @classmethod
  def user_conversations(cls, user_id):
    pipeline = [
      {
        "$match": {
          "user_id": user_id
        }
      },
      {
        "$lookup": {
          "from": "messages",
          "localField": "messages",
          "foreignField": "_id",
          "as": "message_details"
        }
      },
      {
        "$project": {
          "_id": { "$toString": "$_id" },
          "name": 1,
          "created_at": { "$dateToString": { "format": "%d/%m/%Y %H:%M:%S", "date": "$created_at" }},
          "updated_at": { "$dateToString": { "format": "%d/%m/%Y %H:%M:%S", "date": "$updated_at" }},
          "message_count": { "$size": "$message_details" }
        }
      }
    ]
    # execute aggregate
    results = cls._get_collection().aggregate(pipeline)
    return list(results)
  
  @classmethod
  def conversation_messages(cls, conversation_id): # (str)
    pipeline = [
      {
        "$match": {
          "_id": ObjectId(conversation_id)
        }
      },
      {
        "$lookup": {
          "from": "messages",
          "localField": "messages",
          "foreignField": "_id",
          "as": "message_details"
        }
      },
      {
        "$unwind": {
          "path": "$message_details",
          "preserveNullAndEmptyArrays": True
        }
      },
      {
        "$group": {
          "_id": {
            "conversation_id": "$_id",
            "name": "$name",
            "created_at": {
              "$dateToString": {
                "format": "%d/%m/%Y %H:%M:%S",
                "date": "$created_at"
              }
            },
            "updated_at": {
              "$dateToString": {
                "format": "%d/%m/%Y %H:%M:%S",
                "date": "$updated_at"
              }
            }
          },
          "messages": {
            "$push": {
              "answer": {
                "columns": "$message_details.answer.columns",
                "result_set": "$message_details.answer.result_set",
                "query": "$message_details.answer.query",
                "_id": { "$toString": "$message_details.answer._id" }
              },
              "question": "$message_details.question",
              "error": "$message_details.error",
              "created_at": {
                "$dateToString": {
                  "format": "%d/%m/%Y %H:%M:%S",
                  "date": "$message_details.created_at"
                }
              }
            }
          }
        }
      },
      {
        "$project": {
          "_id": 0,
          "id": { "$toString": "$_id.conversation_id" },
          "name": "$_id.name",
          "created_at": "$_id.created_at",
          "updated_at": "$_id.updated_at",
          "messages": 1
        }
      },
      {
        "$limit": 1
      }
    ]
    # execute aggregate
    results = cls._get_collection().aggregate(pipeline)
    results = list(results)
    if len(results) == 1:
      return results[0]
    else:
      return {}