from mongoengine import Document,StringField, IntField, ListField
import mlab

mlab.connect()

class Post(Document):
    tit = StringField()
    descript = StringField()
    img = StringField()
    user = StringField()
    like = IntField()  
    wholike = ListField() 
    comment = ListField()   

