from flask import Flask
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///chaithra.db"
db.init_app(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String)

with app.app_context():
    db.create_all()



@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__=='__main__':
    app.run()

