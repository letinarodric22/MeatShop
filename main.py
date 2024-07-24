from flask import Flask, render_template, redirect, request
from database import *
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")

@app.route("/students")
def students():
   user = users("users")
   return render_template("students.html", user = user)



@app.route("/register")
def register():
   return render_template("register.html")

@app.route('/courses')
def courses():
    course = fetch_data("courses")
    return render_template("courses.html", course=course)


@app.route('/adduser', methods=["POST", "GET"])
def addproducts():
   if request.method=="POST":
      fullname = request.form["fullname"]
      email = request.form["email"]
      user_type=request.form["user_type"]
      user_status = request.form["user_status"]
      password1 = request.form["password"]
      password = generate_password_hash(password1)
      dob = request.form["dob"]
      user=(fullname,email,user_type, user_status, password, 'now()',dob)
      insert_user(user)
      return redirect("/register")
   
   # @app.route('/login', methods=["POST", "GET"])
   # def login():
   #    if request.method=='POST':
   #           email = request.form["email"]
   #           password = request.form["password"]

   
   

  

if __name__ == '__main__':

    app.run(debug=True)
    