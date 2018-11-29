from flask import Flask, render_template, request
import mlab
from addbike import AddBike 

mlab.connect() 
app = Flask(__name__) 

@app.route("/new_bike", methods= ["GET", "POST"])
def new_bike(): 
    if request.method == "GET": 
        return render_template("ex1_addBike.html")
    elif request.method == "POST":
        # Save database 
        form = request.form 
        m = form["Model"] 
        daily = form["DailyFee"]
        img = form["Image"]
        y = form["Year"]
        exist = AddBike.objects(Model= m, Image= img, Year= y).first()
        if exist != None:
            return "exist :3 "
        else:
            i = AddBike(Model= m, DailyFee= daily, Image= img, Year= y)
            i.save()
            return "ok!! :v "


if __name__ == "__main__":
    app.run(debug= True)