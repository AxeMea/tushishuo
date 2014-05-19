from flask import Blueprint,request

sns_blue = Blueprint('sns_blue',__name__,url_prefix='/auth')

@sns_blue.route('/index')
def index():
	print 'hello'
	return 'what the fuck'
