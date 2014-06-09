#encoding: utf-8
from flask import Blueprint,request,render_template,g,session,redirect,url_for
from core.module.sns.service import *
from core.module.sns.forms import *
from core.module.sns.service import *
from core.share.model.models import *
from flask_login import LoginManager,login_user,logout_user,login_required
from core import login_manager,app
import time

sns_blue = Blueprint('sns_blue',__name__,url_prefix='/auth')


#login view
@sns_blue.route('/login',methods=['GET','POST'])
def login():
	form = LoginForm(request.form)

	if form.validate():
		user = User.query.filter_by(email = form.email.data,password = form.password.data).first()

		if user is None:
			return render_template('/sns/index.html',login_form = form)
		else:
			login_user(user)
			return render_template('/sns/index.html',current_user = {'username':user.username})

	return  render_template('/sns/index.html',form=form)


#index view
@sns_blue.route('/index',methods=['POST','GET'])
def index():
	login_form = LoginForm()
	register_form = RegisterForm()

	#推荐故事
	storys = get_recommand_storys()
	#精彩评论
	comments = get_good_comments()
	#热门主题
	themes = get_index_themes()
	return render_template('/sns/index.html',login_form = login_form,register_form = register_form)


#logout view
@sns_blue.route('/logout',methods=['POST','GET'])
@login_required
def logout():
	logout_user()
	return redirect('/auth/index')

@login_manager.user_loader
def load_user(id):
	return User.query.get(int(id))

@sns_blue.route('/register',methods=['GET',"POST"])
def register():
	form = RegisterForm(request.form)
	if form.validate():
		user = User(email = form.email.data,
			    username = form.last_name.data +  form.first_name.data,
			    password = form.password.data,
			    register_date = time.time(),
			    login_latest_date = time.time())
		db.session.add(user)
		db.session.commit()
	return redirect('/auth/index')





