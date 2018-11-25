import mlab
from river import River

mlab.connect() 

#search
#ex2
records = River.objects(continent= 'Africa')
for river in records:
    print(river.name, river.continent, river.length, sep= '\n')
    print("*******************")

print("-------------------")
#ex3
records = River.objects(continent= "S. America", length__lt= 1000) 
for river in records:
    print(river.name, river.continent, river.length, sep= '\n')
    print("*******************") 



 