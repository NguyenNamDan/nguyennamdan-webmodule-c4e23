from flask import Flask, redirect

app = Flask(__name__)

@app.route("/about-me")
def aboutMe():
    about = '''
    Name: Nguyen Nam Dan
    Work: Student
    School: HUST
    Hobbies: movie, listen to music, sport, rubik
    Crush: ... :v
    '''
    return about 

@app.route("/school")
def school():
    return redirect("http://www.techkids.vn") 

if __name__ == "__main__": #Ctrl + C -> machine auto run 
    app.run(debug=True) 