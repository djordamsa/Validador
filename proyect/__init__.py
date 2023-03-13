import os
from flask import Flask
from dotenv import load_dotenv
from pymongo import MongoClient

from proyect.routes import pages

load_dotenv()


def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = os.environ.get(
        "SECRET_KEY", "pf9Wkove4IKEAXvy-cQkeDPhv9Cb3Ag-wyJILbq_dFw"
    )
    app.config['UPLOAD_FOLDER'] = 'static/files'
    app.register_blueprint(pages)
    return app