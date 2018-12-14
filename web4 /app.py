from flask import Flask, render_template, request, session, redirect, url_for
from models.user import User
from models.movie import Movie 
import mlab

mlab.connect() 
app = Flask(__name__)
app.config["SECRET_KEY"] = "namdan" #key mở két 

@app.route("/profile")
def profile():
    if "token" in session:
        username = session["token"]
        user = User.objects(username=username).first() 
        movies = Movie.objects(user= user)
        for m in movies:
            print(m.title) 
        return render_template("profile.html", movies= movies)  
    else:
        return "fail"

@app.route("/login", methods= ["GET", "POSt"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        form = request.form 
        username = form["username"]
        password = form["password"]
        found_user = User.objects(username= username).first()
        if found_user is None:
            return "No such user"
        elif found_user.password != password:
            return "Fail"
        else:
            session["token"] = username #token
            return "ok :v"

@app.route("/logout")
def logout():
    if "token" in session:
        del session["token"] #delete token
    return redirect(url_for("login"))

@app.route("/add_movie", methods=["GET", "POST"])
def add_movie():
    if "token" not in session:
        return redirect("/login")
    if request.method == "GET":
        return render_template("add_movie.html")
    elif request.method == "POST":
        form = request.form 
        title = form["title"]
        image = form["image"]
        year = form["year"]
        username = session["token"] 
        user = User.objects(username= username).first() 
        new_movie = Movie(title= title, image= image, year= year, user= user)  
        new_movie.save() 
        return "OK :D "

if __name__ == '__main__':
  app.run(debug=True)