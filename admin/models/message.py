from mongoengine import DateTimeField, BooleanField, EmbeddedDocument, Document, ObjectIdField, StringField, EmbeddedDocumentField
from bson import ObjectId
from datetime import datetime
from admin.models.answer import Answer

class Message(Document):
  id = ObjectIdField(primary_key=True) 
  question = StringField()
  answer = EmbeddedDocumentField(Answer)
  error = BooleanField()
  created = DateTimeField(default=datetime.utcnow)
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
      created=data.get('created', datetime.utcnow())
    )

  def to_map(self):
    return {
      'id': str(self.id),
      'question': self.question,
      'answer': self.answer.to_map() if self.answer else None,
      'error': self.error,
      'created': self.created.isoformat()
    }

  def __str__(self):
    return (f"Message(id={self.id}, question='{self.question}', "
        f"answer={self.answer}, error={self.error}, "
        f"created={self.created.isoformat()})")