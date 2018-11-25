#design
from mongoengine import Document, StringField, IntField, FloatField, BooleanField

#kế thừa Document
class Resource(Document):
    meta = {
        "strict": False,
    }
    name = StringField()
    city = StringField() 
    yob = IntField()
    height = FloatField()
    weight = FloatField()
    available = BooleanField(default= False)   
