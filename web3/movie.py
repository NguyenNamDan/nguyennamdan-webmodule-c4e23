#design
from mongoengine import Document, StringField, IntField

#kế thừa Document
class Movie(Document):
    title = StringField()
    image = StringField()
    year = IntField()
    
