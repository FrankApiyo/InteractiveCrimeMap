import datetime

from config import DevConfig
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate
from flask import render_template 
from flask import request 
from faker import Faker 

app = Flask(__name__)
app.config.from_object(DevConfig)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
fake = Faker()

class Crime(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    latitude = db.Column(db.Float())
    logintude = db.Column(db.Float())
    date = db.Column(db.DateTime(), default=datetime.datetime.now)
    cartegory = db.Column(db.Text(), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    updated_at = db.Column(db.DateTime(), default=datetime.datetime.now)

    def __init__(self, logitude, latitude, cartegory, description):
        self.logitude = logitude
        self.latitude = latitude 
        self.cartegory = cartegory
        self.description = description

    def __repr__(self):
        return "<Crime at '{}, {}': {}>".format(self.logitude, self.latitude, self.cartegory)


@app.route('/')
def home():
    #here will get all the crimes from our database and put in a local variable called data 
    #db.create_all()
    data = Crime.query.all()

    return render_template("home.html", data=data)

@app.route("/add", methods=["post"])
def add():
    #this method adds a crime to the database so we will improve it so we can add all the fields to the database
    #all these data fields are expected to come from the user
    description  = request.form.get("description")
    longitude =  fake.latitude()
    latitude = fake.longitude()
    cartegory = request.form.get("cartegory")

    crime = Crime(longitude, latitude, cartegory, description)

    #now simply add crime to the database
    db.session.add(crime)
    db.session.commit()

    return home()

@app.route("/clear")
def clear():
    #clear all data from the database (meaning the Crime table)
    db.session.query(Crime).delete()
    db.session.commit()

    return home()


if __name__ == "__main__":
    app.run()