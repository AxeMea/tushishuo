#encoding: utf-8    
from flask import Flask
from flask_sqlalchemy import SQLAlchemy # @UnresolvedImport
from flask_login import LoginManager # @UnresolvedImport
import logging,MySQLdb
from core.config.config import *

app = Flask(__name__)
app.secret_key = 'why would I tell you my secret key?'

app.config.from_object('config')

db = SQLAlchemy(app)

from core.share.model.models import *

if(INIT_DATABASE):
	db.create_all()

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "/index.html"
  
#logging.basicConfig(filename=dirname(__file__)+"/blueprint.log", level=logging.INFO, filemode='a', format='%(asctime)s - %(levelname)s: %(message)s')

from core.module.sns.views import  sns_blue 
app.register_blueprint(sns_blue)

