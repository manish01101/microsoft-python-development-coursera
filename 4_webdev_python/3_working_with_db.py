from flask_sqlalchemy import SQLAlchemy  # Flask-Migrate for migration
from flask import Flask

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URL"] = "sqllite3://my_flask_app.db"
db = SQLAlchemy(app)

"""Implementing one-to-one relationships in Flask (SQLAlchemy)"""


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(120), unique=True, nullable=False)
    profile = db.relationship("UserProfile", backref="user", uselist=False)


class UserProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bio = db.Column(db.Text)
    profile_picture = db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))


"""Implementing one-to-many relationships in Flask (SQLAlchemy)"""


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    posts = db.relationship("Post", backref="blog")


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    content = db.Column(db.Text)
    blog_id = db.Column(db.Integer, db.ForeignKey("blog.id"))


"""Implementing many-to-many relationships in Flask (SQLAlchemy)"""
enrollments = db.Table(
    "enrollments",
    db.Column("student_id", db.Integer, db.ForeignKey("student.id"), primary_key=True),
    db.Column("course_id", db.Integer, db.ForeignKey("course.id"), primary_key=True),
)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    courses = db.relationship(
        "Course", secondary=enrollments, backref=db.backref("students", lazy="dynamic")
    )


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))


# identify all "active" customers from your database.
active_customers = session.query(Customer).filter(Customer.is_active == True).all()

# pinpoint customers who are either "active" and have made a purchase within the last 30 days, or who hold the esteemed "VIP" status
from datetime import datetime, timedelta

thirty_days_ago = datetime.now() - timedelta(days=30)

customers = (
    session.query(Customer)
    .filter(
        or_(
            and_(
                Customer.is_active == True,
                Customer.last_purchase_date >= thirty_days_ago,
            ),
            Customer.is_vip == True,
        )
    )
    .all()
)

# retrieve all orders placed by customers residing in a specific city
orders = session.query(Order).join(Customer).filter(Customer.city == "New York").all()

# To retrieve a list of customers sorted alphabetically by their last name
customers = session.query(Customer).order_by(Customer.last_name).all()

# To obtain the latest orders first
orders = session.query(Order).order_by(Order.order_date.desc()).all()

# categorize customers first by their city, and then alphabetically by last name within each city
customers = session.query(Customer).order_by(Customer.city, Customer.last_name).all()

# total number of orders in your system, a simple aggregation query using the count()
total_orders = session.query(func.count(Order.id)).scalar()

# average order
avg_order_value = session.query(func.avg(Order.total_amount)).scalar()

# calculate the total sales for each product in your inventory.
from sqlalchemy import func

product_sales = (
    session.query(
        OrderItem.product_id,
        func.sum(OrderItem.quantity * OrderItem.unit_price).label("total_sales"),
    )
    .group_by(OrderItem.product_id)
    .all()
)
