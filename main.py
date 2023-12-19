from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, TextAreaField
from wtforms.validators import DataRequired, URL, Email
from datetime import date
import smtplib
import os


my_email = os.environ.get("EMAIL")
my_password = os.environ.get("PASSWORD")

app = Flask(__name__)

class ContactForm(FlaskForm):
    name = StringField(validators=[DataRequired()], render_kw={"placeholder": "Your Name"})
    email = EmailField(validators=[DataRequired(), Email()], render_kw={"placeholder": "Your Email"})
    subject = StringField(validators=[DataRequired()], render_kw={"placeholder": "Subject"})
    message = TextAreaField(validators=[DataRequired()], render_kw={"placeholder": "Message"})
    submit = SubmitField(label="Send Message")

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

@app.route("/contact", methods=["POST", "GET"])
def contact():
    form = ContactForm()
    
    msg = f"Hello,\nThis mail is from {form.name.data} with the mailadress: {form.email.data}\n\n{form.message.data}"
    
    if form.validate_on_submit():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=my_email,
                msg=f"Subject:{form.subject.data} \n\n{msg}"
            )
            redirect(url_for("home"))
    
    return render_template("contact.html", form=form)

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
    app.run(debug=True)