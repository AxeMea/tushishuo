from flask import Blueprint,request,render_template
from core.module.sns.service import *
from core.module.sns.forms import *

sns_blue = Blueprint('sns_blue',__name__,url_prefix='/auth')

@sns_blue.route('/index',methods=['GET','POST'])
def index():
	form = LoginForm()
	return  render_template('/sns/index.html',form=form)
