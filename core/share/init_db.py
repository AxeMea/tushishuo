from flask_sqlalchemy import SQLAlchemy 
import MySQLdb

def init_db(app):
	db = SQLAlchemy(app)
	db.create_all()


class User(db.Model):
	__tablename__ = 'ngu_user'

    	uuid = db.Column(db.Integer, primary_key=True)
    	username = db.Column(db.String(256))
    	email = db.Column(db.String(256))
	register_date = db.Column(db.Date)
	login_latest_date = db.Column(db.Date)

    	def __init__(self, username,emial):
        	self.username = username
        	self.email = email

    	def __repr__(self):
        	return '<User %r>' % self.username

class Picture(db.Model):
	__tablename__ = 'ngu_picture'

    	uuid = db.Column(db.Integer, primary_key=True)
    	path = db.Column(db.String(256))
    	upload_user = db.Column(db.String(256))
	upload_time = db.Column(db.String(256))
	like = db.Column(db.Integer())
	dislike = db.Column(db.Interger)
	note = db.Column(db.String(1024)) 

    	def __init__(self, path):
        	self.username = username
        	self.email = email

    	def __repr__(self):
        	return '<Picture %r>' % self.username


class Theme(db.Model):
	__tablename__ = 'ngu_theme'

	uuid = db.Column(db.Integer, primary_key=True) 
	note = db.Column(db.String(1024))



class ThemeMapping(db.Model):
	__tablename__ = 'ngu_thememapping'
	
	uuid = db.Column(db.Integer, primary_key=True)
	theme = db.Column(db.Integer)
	picture = db.Column(db.Integer)


class Story(db.Model):
	__tablename__ = 'ngu_story'

	uuid = db.Column(db.Integer, primary_key=True)
	author = db.Column(db.Integer)
	theme = db.Column(db.Integer)
	update_time = db.Column(db.Date)
	content = db.Column(db.Text)
	like = db.Column(db.Integer)


class Comment(db.Model):
	__tablename__ == 'ngu_comment'

	uuid = db.Column(db.Integer, primary_key=True)
 	story = db.Column(db.Integer)
	content = db.Column(db.Text)


class Follow(db.Model):
	__tablename__ = 'ngu_follow'

 	uuid = db.Column(db.Integer, primary_key=True)
	follow = db.Column(db.Integer)
	followed = db.Column(db.Integer)

class Feed(db.Model):
	__tablename__ = 'ngu_feed'

	uuid = db.Column(db.Integer, primary_key=True)
	author = db.Column(db.Integer)
	content = db.Column(db.Text)
	publish_date = db.Column(db.Date)	
