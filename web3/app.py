from flask import Flask, render_template, request
import mlab
from register import Register
from gmail import GMail, Message


mlab.connect() 
app = Flask(__name__)

@app.route("/add_movie", methods=["GET", "POST"])
def add_movie():
    if request.method == "GET": #user request GET form
        return render_template("add_movie.html") 
    elif request.method == "POST": #request POST form 
        # Save database 
        form = request.form 
        t = form["title"]
        img = form["image"]
        y = form["year"]
        m = Movie(title=t, image=img, year= y) 
        m.save() 
        return "ok :v "

@app.route("/register", methods= ["GET", "POST"])
def register(): 
    if request.method == "GET": #user request GET form
        return render_template("register.html")  
    elif request.method == "POST": #request POST form
        form = request.form 
        name = form["username"]
        pw = form["password"]
        em = form["email"]
        exist_user = Register.objects(username= name).first()
        if exist_user != None: 
            return "exist :3"
        else:
            m = Register(username= name, password= pw, email_check= em) 
            m.save()
            # gmail = GMail("hiimdangoilaxiit2610@gmail.com", "nnd26101999")
            # message = Message("bạn đã đăng kí thành công! :v ", to=em)
            # gmail.send(message)  
            return "ok :v hihi"
if __name__ == "__main__":
    app.run(debug= True)  