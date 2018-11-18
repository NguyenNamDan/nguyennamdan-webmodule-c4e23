from flask import Flask,render_template 

app = Flask(__name__)

@app.route("/bmi/<int:weight>/<int:height>")
def bmi(weight, height):
    heightM = height/100
    bmiIndex = weight/(heightM**2) 
    return render_template("bmi.html", BMI= bmiIndex) 

if __name__ == "__main__": #Ctrl + C -> machine auto run 
    app.run(debug=True)

