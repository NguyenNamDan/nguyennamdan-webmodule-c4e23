import mlab
from models.movie import Movie
from models.user import User 

mlab.connect() 
# Movie.drop_collection() #xoa full movie

for movie in Movie.objects():
    print(movie.title) 
    print(movie.user.username)  