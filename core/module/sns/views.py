from flask import Blueprint,request,render_template
from core.module.sns.service import *

sns_blue = Blueprint('sns_blue',__name__,url_prefix='/auth')

@sns_blue.route('/index',methods=['GET','POST'])
def index():
	return  render_template('index.html')
