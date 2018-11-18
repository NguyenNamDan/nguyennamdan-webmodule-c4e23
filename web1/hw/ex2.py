from flask import Flask, render_template

app = Flask(__name__)

@app.route("/user/<username>")
def user(username):
    users = {
        "huy": {
            "name": "Nguyen Quang Huy",
            "gender": "Male",
            "age": 29
        },
        "tuananh": {
            "name": "Huynh Tuan Anh",
            "gender": "Male",
            "age": 22
        },
        "namdan": {
            "name": "Nguyen Nam Dan",
            "gender": "Male",
            "age": 19
        }
    }
    if username in users.keys(): 
        return render_template("username.html", name=users[username])
    else:
        return "User not found"
if __name__ == "__main__": #Ctrl + C -> machine auto run 
    app.run(debug=True)
