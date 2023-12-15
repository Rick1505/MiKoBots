from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, TextAreaField
from wtforms.validators import DataRequired, URL
from datetime import date
import smtplib
import os


my_email = os.environ.get("EMAIL")
my_password = os.environ.get("PASSWORD")

app = Flask(__name__)

# SET UP A ENV SECRET KEY
app.config['SECRET_KEY'] = os.environ.get("FLASK_KEY")
Bootstrap5(app)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/blog")
def blog():
    return render_template("blog.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/feature")
def feature():
    return render_template("feature.html")

@app.route("/product")
def product():
    return render_template("product.html")

@app.route("/store")
def store():
    return render_template("store.html")

@app.route("/testimonial")
def testimonial():
    return render_template("testimonial.html")

@app.route("/countdown")
def countdown():
    return render_template("countdown.html")

if __name__ == "__main__":
    app.run(debug=False)