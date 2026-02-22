import logging

# Configure the logging module
logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Log some messages
logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")

from flask import Flask


app = Flask(__name__)

# Configure Logging
logging.basicConfig(
    filename="flask_app.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


@app.route("/")
def index():
    logging.info("Home page accessed")
    return "Hello, world!"


if __name__ == "__main__":
    app.run(debug=True)
