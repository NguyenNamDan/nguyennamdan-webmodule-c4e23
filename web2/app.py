#main chính
import mlab
from movie import Movie
from resource import Resource
from faker import Faker #data giả 
from random import randint

faker = Faker("en_US")  
# for _ in range(5):
#     print(faker.state())

mlab.connect() #connect

#(DELETE)
# m = Movie.objects().with_id("5bf7f9befa0d7271ed1eda74") #find id
# m.delete() 

# m = Resource.objects()[1] #find index 
# m.delete()  

#(READ)
# movie_list = Movie.objects() 

# for m in movie_list:
#     print(m.title, m.image, m.year, sep= '\n')  

# resource_list = Resource.objects()

# for i in resource_list:
#     print(i.name, i.city, i.yob, i.height, i.weight, sep= '\n')


#tao data (CREATE)
# m = Resource(name= 'Nguyen Nam Dan', city= 'Hung Yen', yob= 1999, height= 170, weight= 53.5)

# m.save()  #Save

#(FAKER) 
# for _ in range(100):
#     name = faker.name()
#     city = faker.state()
#     yob = randint(1953, 2000)
#     height = randint(150, 200)
#     weight = randint(40, 150)
#     r = Resource(name= name, city= city, yob= yob, height= height, weight= weight)
#     r.save()  

#(SEARCH) 
# records = Resource.objects(name= "James Levy")
# for i in records:
#     print(i.name, i.city, i.yob, sep= '\t')

# records = Resource.objects(height= 172)
# for i in records:
#     print(i.name, i.city, sep= '\t')

# records = Resource.objects(name__icontains= 'james')
# print(len(records)) 

# records = Resource.objects(height__gt= 160, name__icontains= 'Tina')
# for i in records:
#     print(i.name, i.city, i.yob, sep= '\n') 

#(UPDATE)
# records = Resource.objects()
# for r in records:
#     r.update(set__available= False)

# r = Resource.objects().with_id("5bf80de6fa0d727f2f329e7a")
# r.update(set__available= True) 






