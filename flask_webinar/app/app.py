from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config.update(
    SQLALCHEMY_DATABASE_URI='postgresql://postgres:postgres@db:5432/netology_flask',
    JSON_SORT_KEYS=False
)

db = SQLAlchemy(app)
ma = Marshmallow(app)
