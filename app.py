from flask import Flask, request, jsonify
from database import db
from models.user import User
from flask_login import LoginManager, login_user, current_user

app = Flask(__name__)
app.config["SECRET_KEY"] = "YOUR SECRET KEY"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

# Initialize db with the app context
login_manager = LoginManager()
db.init_app(app)
login_manager.init_app(app)

login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route("/init", methods=["GET"])
def init_func():
    with app.app_context():
        db.create_all()
    return "Database initialized"


@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username and password:
        user = User.query.filter_by(username=username).first()
        if user is None:
            return jsonify({"message": "Not found"}), 404
        if user and user.password == (password):
            login_user(user)
            return jsonify({"message": "Login successful", "current_user": user.username}), 200
        else:
            return jsonify({"message": "Invalid credentials"}), 400
    else:
        return jsonify({"message": "Invalid credentials"}), 400


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
