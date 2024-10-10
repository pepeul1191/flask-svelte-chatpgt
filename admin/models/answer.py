from mongoengine import DateTimeField, FloatField, EmbeddedDocument, ObjectIdField, StringField, ListField
from bson import ObjectId

class Answer(EmbeddedDocument):
  id = ObjectIdField(primary_key=True) 
  query = StringField()
  result_set = ListField()
  columns = ListField()
  meta = {
    'collection': 'answers'  # Nombre de la colección a la que deseas mapear
  }

  @classmethod
  def from_map(cls, data):
    return cls(
      id=data.get('id', ObjectId()),
      query=data.get('query'),
      result_set=data.get('result_set', []),
      columns=data.get('columns', [])
    )

  def to_map(self):
    return {
      '_id': str(self.id),
      'query': self.query,
      'result_set': self.result_set,
      'columns': self.columns
    }

  def __str__(self):
    return f"Answer(_id={self.id}, query='{self.query}', result_set={self.result_set}, columns={self.columns})"