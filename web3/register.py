#design
from mongoengine import Document, StringField, BooleanField

#kế thừa Document
class Register(Document):
    username = StringField()
    password = StringField()
    email_check = BooleanField(default=False)  
