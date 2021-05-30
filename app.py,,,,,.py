# 121290, 123013, 120090, 123701, 123201, 122185
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config[ 'SQLALCHEMY_DATABASE-URI'] ='sqlite:///test.db'

db =SQLAlchemy(app)

class UsersDetails(db.model):
   id=db.Column(db.integer,primary_key=True)
   firstname=db.Column(db.String(250), nullable=False)
   lastname=db.Column(db.String(250),nullable=False)
   email=db.Column(db.String(250), nullable=False)
   message=db.Column(db.String(2000),nullable=False)

   def__repr__(self):
      return '<UsersDetails %r>' %self.id

@app.route("/home")
def home():
    return render_template('index.html')


@app.route("/contact", methods=["GET","POST"])
def contact():
    if request.method =='POST':
       email =request.form.get('email')
       firstname = request.form.get('firstname')
       lastname = request.form.get('lastname')
       message = request.form.get('message')
       new_contact = UsersDetails(email=email,firstname=firstname,lastname=lastname,message=message)

       db.session.add(new_contact)
       db.session.commit()

       return redirect(url_for('home'))


    return render_template('contact.html')


if__name__== "__main__":
   app.run(debug=True) 
