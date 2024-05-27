from flask import Flask, request, jsonify
from database import db
from models.user import User

app = Flask(__name__)
app.config["SECRET_KEY"] = "YOUR SECRET KEY"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

# Initialize db with the app context
db.init_app(app)


@app.route("/init", methods=["GET"])
def init_func():
    with app.app_context():
        db.create_all()
    return "Database initialized"


@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "404 Not Found: The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again."}), 404


@app.errorhandler(Exception)
def handle_exception(e):
    response = {
        "error": str(e)
    }
    return jsonify(response), 500


if __name__ == "__main__":
    app.run(debug=True)
