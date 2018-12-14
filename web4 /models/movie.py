#design
from mongoengine import *

#kế thừa Document
class Movie(Document):
    title = StringField()
    image = StringField()
    year = IntField()
    user = ReferenceField("User") #tro toi 1 thang khac (User)
    
