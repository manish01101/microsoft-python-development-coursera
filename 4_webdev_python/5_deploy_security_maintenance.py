# 1. Setting Up a Flask Application
from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

df = pd.DataFrame({"Team": ["Team A", "Team B", "Team C"], "Score": [10, 20, 15]})


@app.route("/")
def home():
    return render_template(
        "index.html", tables=[df.to_html()], titles=df.columns.values
    )


if __name__ == "__main__":
    app.run(debug=True)
# Always use the debug=True mode during local development. This allows you to see detailed error messages, which are helpful when something goes wrong.


# 2. Preparing the Application for Production
# Creating a requirements.txt file
# Configuring the host like below
if __name__ == "__main__":
    app.run(
        debug=False, host="0.0.0.0"
    )  # app should be accessible beyond your local machine


# 4. Basic Security for Flask Applications: Implementing input validation
#  Flask-WTF, an extension of Flask, helps in validating form inputs to ensure user data is clean and safe.

from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = os.urandom(24)


class MyForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    submit = SubmitField("Submit")


@app.route("/form", methods=["GET", "POST"])
def form():
    form = MyForm()
    if form.validate_on_submit():
        name = form.name.data
        return f"Hello, {name}!"
    return render_template("form.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)


"""
Load testing tools, such as Azure Load Testing, can simulate thousands of concurrent users, allowing developers to observe how the system behaves under heavy load

Microsoft Playwright provide virtual environments where developers can test their application on various combinations of browsers and operating systems. This allows them to identify and fix issues specific to certain configurations, ensuring that the application looks and behaves as intended, regardless of the user's technology choices.  
"""
