from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from my_scripts.happy_functions import make_word

app = Flask(__name__)

ENV = 'prod'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = ''
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://pqdkomxluldtul:56ab90f93e1069af21870f7d1415e9e1b06a1c53d9710b5ecd20ce5466f338b0@ec2-3-209-65-193.compute-1.amazonaws.com:5432/dcccaj5caml9jc'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)