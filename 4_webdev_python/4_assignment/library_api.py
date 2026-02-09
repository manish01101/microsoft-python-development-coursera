from flask import Flask, jsonify, request, abort
from flask_restful import Api, Resource
from flask_restful.reqparse import RequestParser

app = Flask(__name__)
api = Api(app)

# In-memory database
BOOKS = {
    "1": {
        "title": "The Hitchhiker's Guide to the Galaxy",
        "author": "Douglas Adams",
        "publication_year": 1979,
    },
    "2": {
        "title": "1984",
        "author": "George Orwell",
        "publication_year": 1949,
    },
    "3": {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "publication_year": 1960,
    },
}

# Request parser for POST
parser = RequestParser()
parser.add_argument("title", type=str, required=True, help="Title is required")
parser.add_argument("author", type=str, required=True, help="Author is required")
parser.add_argument(
    "publication_year", type=int, required=True, help="Publication year is required"
)


# Simple authentication
def authenticate(username, password):
    return username == "admin" and password == "password"


class Books(Resource):
    def get(self):
        search_query = request.args.get("search")
        if search_query:
            results = [
                book
                for book in BOOKS.values()
                if search_query.lower() in book["title"].lower()
                or search_query.lower() in book["author"].lower()
            ]
            return jsonify(results)

        return jsonify(BOOKS)

    def post(self):
        auth = request.authorization
        if not auth or not authenticate(auth.username, auth.password):
            abort(401, description="Authentication required")

        args = parser.parse_args()
        new_id = str(int(max(BOOKS.keys(), default="0")) + 1)
        BOOKS[new_id] = {
            "title": args["title"],
            "author": args["author"],
            "publication_year": args["publication_year"],
        }
        return jsonify(BOOKS[new_id])


class Book(Resource):
    def get(self, book_id):
        if book_id not in BOOKS:
            abort(404, description="Book not found")
        return jsonify(BOOKS[book_id])


# Register endpoints
api.add_resource(Books, "/books/")
api.add_resource(Book, "/books/<string:book_id>")


if __name__ == "__main__":
    app.run(debug=True)
