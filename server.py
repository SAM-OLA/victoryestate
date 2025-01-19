from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float


app = Flask(__name__)

class Base(DeclarativeBase):
    pass
 
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///victoryresidents.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)

@app.route('/')
def home():
    return render_template('index.html',)

@app.route('/aboutus')
def about_us():
    return render_template("aboutus.html")

@app.route('/contactus')
def contact_us():
    return render_template("contactus.html")

@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/<name>')
def greet(name):
    return f'Hello there {name}!'


if __name__ == '__main__':
    app.run(debug=True)