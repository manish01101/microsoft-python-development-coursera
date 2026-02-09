from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
"""
flask db init        # only once, first time
flask db migrate     # generate migration
flask db upgrade     # apply migration
"""


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)


@app.route("/create-user")
def create_user():
    user = User(username="Manish", email="manish@test.com")
    db.session.add(user)
    db.session.commit()
    return "User created"


if __name__ == "__main__":
    app.run(debug=True)
