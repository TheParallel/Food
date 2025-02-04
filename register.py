from flask import Blueprint,render_template,request
from pymongo import MongoClient

reg = Blueprint('register',__name__,template_folder='templates')
@reg.route("/register",methods=['GET','POST'])
def regr():
    return render_template("register.html")

@reg.route("/onboarding",methods=['POST'])
def onboarding():
    client = MongoClient("mongodb+srv://tejas:1234@pocketsdb-i09wt.mongodb.net/test?retryWrites=true&w=majority")
    fname = str(request.form['fname'])
    lname = str(request.form['lname'])
    email = str(request.form['email'])
    passw = str(request.form['psw'])
    db = client.userdb
    db.userDetails.insert_one({"fname":fname,"lname":lname,"email":email})
    db = client.logindb
    db.loginAuth.insert_one({"user":email,"passw":passw})
    db = client.emails
    db.emailDB.insert_one({"email":email})
    client.close()
    return render_template("address.html")
@reg.route("/address",methods=["GET","POST"])
def address():
    client = MongoClient("mongodb+srv://tejas:1234@pocketsdb-i09wt.mongodb.net/test?retryWrites=true&w=majority")
    unum = str(request.form['fname'])
    bname = str(request.form['lname'])
    addr1 = str(request.form['email'])
    addr2 = str(request.form['psw'])
    city = str(request.form['psw-repeat'])
    pincode = str(request.form['pincode'])
    db = client.emails
    email = db.emailDB.find_one()["email"]
    db.emailDB.delete_one({"email":email})
    db = client.addressdb
    db.userAddress.insert_one({"email":email,"unum":unum,"bname":bname,"addr1":addr1,"addr2":addr2,"city":city,"pincode":pincode})
    client.close()
    return render_template("hello.html")



    