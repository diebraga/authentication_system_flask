from flask import Flask, request, jsonify
from flask_swagger_ui import get_swaggerui_blueprint
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SECRET_KEY"] = "YOUR SECRET KEY"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

db = SQLAlchemy(app)

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.yaml'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'authentication': "Authentication App"
    }
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)


@app.route("/init", methods=["GET"])
def init_func():
    return "init"


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
