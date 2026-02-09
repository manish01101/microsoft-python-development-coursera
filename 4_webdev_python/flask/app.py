from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route("/")  # decorator
def hello():
    return "hello manish!"


@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        return "post"
    else:
        return "get"


@app.route("/greet/<name>")  # dynamic route
def greet(name):
    return render_template("a.html", name=name)
    # return name


@app.route(
    "/get/<int:post_id>"
)  # `int:` converter within the angle brackets mandates that the `post_id` variable must hold an integer value.
def getId(post_id):
    return post_id


if __name__ == "__main__":
    app.run(debug=True)
