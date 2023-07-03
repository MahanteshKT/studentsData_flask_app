from flask import Flask,render_template,redirect,url_for,request,flash
from db_connect import db_connection
import datetime
app=Flask(__name__)
app.secret_key="flask_app"
col=db_connection()

@app.route("/",methods=['GET','POST'])
def home():
   
    students = col.find().sort("date",-1)
    print(students)
    context={
        "title":"home",
        "students":students
    }
    return render_template("index.html",context=context)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    college = request.form['college']

    student_data = {
        'name': name,
        'college': college,
        "date":datetime.datetime.now(tz=datetime.timezone.utc)
    }
    col.insert_one(student_data)
    flash("students data is successfully added to database",'success')
    return redirect(url_for("home"))



if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0",port="4000")