from flask import Flask

app = Flask(__name__)

@app.route("/bmi/<int:weight>/<int:height>")
def bmi(weight, height):
    heightM = height/100
    bmiIndex = weight/(heightM**2) 
    if bmiIndex < 16:
        return "Body Mass Index: "+ str(bmiIndex)+ " Severely underweight"
    elif bmiIndex < 18.5:
        return "Body Mass Index: "+ str(bmiIndex)+ " Underweight"
    elif bmiIndex < 25:
        return "Body Mass Index: "+ str(bmiIndex)+ " Normal"
    elif bmiIndex < 30:
        return "Body Mass Index: "+ str(bmiIndex)+ " Overweight"
    else:
        return "Body Mass Index: "+ str(bmiIndex)+ " Obese"

if __name__ == "__main__": #Ctrl + C -> machine auto run 
    app.run(debug=True)

