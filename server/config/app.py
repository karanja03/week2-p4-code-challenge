#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate
from config.models import db
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)



with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(port=5556)