from mongoengine import Document, StringField

class Todo(Document):
    name = StringField()
    description = StringField()
