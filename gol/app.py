from flask import *
from models.user import User 
from models.contribute import Contribute
import mlab 

mlab.connect() 
app = Flask(__name__)
app.config["SECRET_KEY"] = "namdan" #key mở két 

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/sign_up", methods= ["GET", "POST"]) 
def sign_up():
    if request.method == "GET":
        return render_template("sign_up.html")
    else:
        form = request.form 
        fullname = form["fullname"]
        username = form["username"]
        email = form["email"]
        password = form["password"]
        confirm = form["confirm"]
        bday = form["bday"]
        gender = form["gender"]
        phone = form["telephone"]
        existUsername = User.objects(username= username).first()
        existEmail = User.objects(email= email).first()

        if  fullname == "" or username == "" or email == "" or password == "" or confirm == "" or bday == "" or gender == "" or phone == "":
            return "Bạn phải điền đầy đủ thông tin"
        if existUsername is not None:
            return "Tên đăng nhập đã tồn tại"
        if existEmail is not None:
            return "Email đã tồn tại"
        if len(username) < 8:
            return "Tên người dùng không khả dụng"
        if len(password) < 8:
            return "Mật khẩu không khả dụng"
        if confirm == password:
            m = User(fullname= fullname, username= username, email= email, password= password, birthday= bday, gender= gender, phone= phone)
            m.save()  #Save
            return redirect("/sign_in")     
        else:
            return "Rất tiếc. Xác nhận mật khẩu sai" 


@app.route("/sign_in", methods= ["GET", "POST"])
def sign_in():
    if request.method == "GET":
        return render_template("sign_in.html")
    else:
        form = request.form 
        username = form["username"] 
        password = form["password"] 
        found_user = User.objects(username= username).first()
        if found_user is None:
            return "Tên đăng nhập không tồn tại"
        elif found_user.password != password:
            return "Rất tiếc. Mật khẩu không chính xác"
        else:
            session["token"] = username #token
            return redirect(url_for("home"))


@app.route("/sign_out")
def sign_out():
    if "token" in session:
        del session["token"] #delete token
    return redirect(url_for("sign_in"))


@app.route("/edit_information", methods= ["GET", "POST"]) 
def edit_information():
    user = User.objects(username= session["token"]).first() 
    if request.method == "GET":
        return render_template("edit_in4.html", user = user)
    else:
        form = request.form 
        fullname = form["fullname"]
        email = form["email"]
        bday = form["bday"]
        gender = form["gender"]
        phone = form["telephone"]   
        if  fullname == "" or email == "" or bday == "" or gender == "" or phone == "":
            return "Bạn phải điền đầy đủ thông tin"
        user.fullname = fullname
        user.email = email 
        user.birthday = bday
        user.gender = gender
        user.phone = phone 
        user.save() 
        return redirect(url_for("home")) 

@app.route("/password1", methods= ["GET", "POST"])
def password1():
    user = User.objects(username= session["token"]).first() 
    if request.method == "GET":
        return render_template("password1.html", user = user)
    else:
        form = request.form
        password = form["password"]
        if password != user.password:
            return "Sai mật khẩu. Hãy thử lại"
        else:
            return redirect(url_for("password2")) 

@app.route("/password2", methods= ["GET", "POST"])
def password2():
    user = User.objects(username= session["token"]).first() 
    if request.method == "GET":
        return render_template("password2.html")
    else:
        form = request.form
        password = form["password"]
        confirm = form["confirm"]
        if password == "" or len(password) < 8:
            return "Vui lòng chọn mật khẩu dài hơn"
        if confirm != password:
            return "Mật khẩu không khớp"
        else:
            user.password = password
            user.save()
            return redirect(url_for("home"))

@app.route("/contribute", methods= ["GET", "POST"])
def contribute():
    if request.method == "GET":
        return render_template("contribute.html")
    else:
        form = request.form 
        title = form["title"]
        st = form["STR"]
        per = form["PER"]
        knl = form["KNL"]
        soc = form["SOC"]
        cre = form["CRE"]

        ctb = Contribute(tit= title, st= st, per= per, knl= knl, soc= soc, cre= cre)
        ctb.save() 
        return redirect(url_for("home")) 


if __name__ == '__main__':
  app.run(debug=True)