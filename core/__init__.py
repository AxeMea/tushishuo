#encoding: utf-8    
from flask import Flask
from flask_sqlalchemy import SQLAlchemy # @UnresolvedImport
from flask_login import LoginManager # @UnresolvedImport
import logging,MySQLdb

app = Flask(__name__)

app.config.from_object('config')

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username
db.create_all()


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "/index.html"
  
#logging.basicConfig(filename=dirname(__file__)+"/blueprint.log", level=logging.INFO, filemode='a', format='%(asctime)s - %(levelname)s: %(message)s')

from ngu.module.sns.views import  sns_blue 
app.register_blueprint(sns_blue)

