from flask import Blueprint,request,render_template,g,session
from core.module.sns.service import *
from core.module.sns.forms import *
from core.share.model.models import *
#from flask_login import LoginManager
#from core import login_manager,app

sns_blue = Blueprint('sns_blue',__name__,url_prefix='/auth')

@sns_blue.route('/login',methods=['GET','POST'])
def login():
	if g.user is not None and g.user.is_authenticated():
		return redirect('/auth/index')

	form = LoginForm(request.form)

	if form.validate():
		user = User.query.filter_by(email = form.email.data).first()

		if user is None:
			return render_template('/sns/index.html',form = form)
		else:
			return render_template('/sns/index.html',current_user = {'username':user.username})

	return  render_template('/sns/index.html',form=form)


@sns_blue.route('/index',methods=['POST','GET'])
def index():
	form = LoginForm()
	return render_template('/sns/index.html',form = form)

@sns_blue.route('/logout',methods=['POST','GET'])
def logout():
	#logout_user()
	return redirect(url_for('auth/index')

#@login_manager.user_loader
#def load_user(id):
#	return User.query.get(int(id))
#@app.before_request
#def before_request():
#    g.user = current_usere
