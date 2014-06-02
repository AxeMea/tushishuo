#encoding: utf-8
from core import db
from sqlalchemy import Column, String, Text,DateTime,Integer

# 用户表
class User(db.Model):
	__tablename__ = 'ngu_user'

	uuid = db.Column(db.Integer, primary_key=True)
	# 用户名
	username = db.Column(db.String(256))
	# 邮箱
	email = db.Column(db.String(256))
	# 注册日期
	register_date = db.Column(db.DateTime)
	# 最新登陆时间
	login_latest_date = db.Column(db.DateTime)

	def __init__(self, **args):
    		self.username = args['username']
    		self.email = args['email']
    		self.register_date = args['register_date']
    		self.login_latest_date = args['login_latest_date']

	def __repr__(self):
    		return '<User %r>' % self.username

	def is_authenticated(self):
		return True

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def get_id(self):
		return unicode(self.id)



# 图片表
class Picture(db.Model):
	__tablename__ = 'ngu_picture'

	uuid = db.Column(db.Integer, primary_key=True)
	# 图片地址
	path = db.Column(db.String(256))
	# 上传用户id
	upload_user = db.Column(db.Integer)
	# 上传时间
	upload_time = db.Column(db.DateTime)
	# 赞
	like = db.Column(db.Integer)
	# 不喜欢
	dislike = db.Column(db.Integer)
	# 描述
	note = db.Column(db.String(1024)) 

	def __init__(self, **args):
    		self.path = args['path']
    		self.upload_user = args['upload_user']
    		self.upload_time = args['upload_time']
    		self.like = args['like']
    		self.dislike = args['dislike']
    		self.note = args['note']

	def __repr__(self):
    		return '<Picture %r>' % self.path

# 主题表
class Theme(db.Model):
	__tablename__ = 'ngu_theme'

	uuid = db.Column(db.Integer, primary_key=True) 
	# 主题标题
	title = db.Column(db.String(256))
	# 主题描述
	note = db.Column(db.String(1024))

	def __init__(self, **args):
    		self.path = args['path']
    		self.title = args['title']
    		self.note = args['note']

	def __repr__(self):
    		return '<Theme %r>' % self.title


# 主题映射
class ThemeMapping(db.Model):
	__tablename__ = 'ngu_thememapping'
	
	uuid = db.Column(db.Integer, primary_key=True)
	# 主题id
	theme = db.Column(db.Integer)
	# 图片id
	picture = db.Column(db.Integer)

	def __init__(self, **args):
    		self.theme = args['theme']
    		self.picture = args['picture']


	def __repr__(self):
    		return '<ThemeMapping %r>' % self.theme

# 故事表
class Story(db.Model):
	__tablename__ = 'ngu_story'

	uuid = db.Column(db.Integer, primary_key=True)
	# 作者id
	author = db.Column(db.Integer)
	# 主题id
	theme = db.Column(db.Integer)
	# 标题
	title = db.Column(db.String(256))
	# 更新时间
	update_time = db.Column(db.DateTime)
	# 内容
	content = db.Column(db.Text)
	# 赞
	like = db.Column(db.Integer)
	# 不喜欢
	dislike = db.Column(db.Integer)

	def __init__(self, **args):
    		self.author = args['author']
    		self.theme = args['theme']
    		self.update_time = args['update_time']
    		self.content = args['content']
    		self.like = args['like']
    		self.title = args['title']
    		self.dislike = args['dislike']

	def __repr__(self):
    		return '<Story %r>' % self.title

# 评论
class Comment(db.Model):
	__tablename__ = 'ngu_comment'

	uuid = db.Column(db.Integer, primary_key=True)
	# 故事id
 	story = db.Column(db.Integer)
 	# 更新时间
	update_time = db.Column(db.DateTime)
 	# 内容
	content = db.Column(db.Text)

	def __init__(self, **args):
    		self.story = args['story']
    		self.update_time = args['update_time']
    		self.content = args['content']

	def __repr__(self):
    		return '<Comment %r>' % self.uuid

# 关注映射
class Follow(db.Model):
	__tablename__ = 'ngu_follow'

 	uuid = db.Column(db.Integer, primary_key=True)
 	# 用户的id
	follow = db.Column(db.Integer)
	# 被关注用户的id
	followed = db.Column(db.Integer)

	def __init__(self, **args):
    		self.follow = args['follow']
    		self.followed = args['followed']

	def __repr__(self):
    		return '<Follow %r>' % self.uuid

# 新鲜事表
class Feed(db.Model):
	__tablename__ = 'ngu_feed'

	uuid = db.Column(db.Integer, primary_key=True)
	# 作者id
	author = db.Column(db.Integer)
	# 内容
	content = db.Column(db.Text)
	# 发布时间
	publish_date = db.Column(db.DateTime)	

	def __init__(self, **args):
    		self.author = args['author']
    		self.content = args['content']
    		self.update_date = args['update_date']


	def __repr__(self):
    		return '<Feed %r>' % self.uuid
