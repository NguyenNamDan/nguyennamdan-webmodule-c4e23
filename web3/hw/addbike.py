from mongoengine import Document, StringField, IntField

class AddBike(Document):
    Model = StringField()
    DailyFee = IntField()
    Image = StringField()
    Year = IntField() 
     