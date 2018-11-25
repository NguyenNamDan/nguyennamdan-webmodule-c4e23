#design
from mongoengine import Document, StringField, IntField

#kế thừa Document
class River(Document):
    name = StringField()
    continent = StringField()
    length = IntField()
    
