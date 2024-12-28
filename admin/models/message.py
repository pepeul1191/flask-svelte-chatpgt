from mongoengine import DateTimeField, BooleanField, FloatField, Document, ObjectIdField, StringField, EmbeddedDocumentField
from bson import ObjectId
from datetime import datetime
from admin.models.answer import Answer

class Message(Document):
  id = ObjectIdField(primary_key=True) 
  question = StringField()
  answer = EmbeddedDocumentField(Answer)
  error = BooleanField()
  created_at = DateTimeField(default=datetime.utcnow)
  db_version = FloatField()
  meta = {
    'collection': 'messages'  # Nombre de la colección a la que deseas mapear
  }

  @classmethod
  def from_map(cls, data):
    return cls(
      id=data.get('id', ObjectId()),
      question=data.get('question'),
      answer=Answer.from_map(data['answer']) if data.get('answer') else None,
      error=data.get('error', False),
      created_at=data.get('created', datetime.utcnow())
    )

  def to_map(self):
    return {
      '_id': str(self.id),
      'question': self.question,
      'answer': self.answer.to_map() if self.answer else None,
      'error': self.error,
      'created_at': self.created_at.isoformat()
    }

  def __str__(self):
    return (f"Message(_id={self.id}, question='{self.question}', "
        f"answer={self.answer}, error={self.error}, "
        f"created_at={self.created_at.isoformat()})")