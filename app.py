import os
from flask import Flask
from controllers.excel_controller import excel_bp


def create_app() -> Flask:
    app = Flask(__name__, template_folder="views/templates")
    app.secret_key = "dev-secret-change-me"
    app.config["UPLOAD_FOLDER"] = os.path.join(os.path.dirname(__file__), "uploads")
    app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024  # 16 MB

    app.register_blueprint(excel_bp)
    return app


if __name__ == "__main__":
    create_app().run(debug=True, host="127.0.0.1", port=5000)
