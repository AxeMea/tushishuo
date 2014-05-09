from flask_sqlalchemy import SQLAlchemy 


def init_db(app):
	db = SQLAlchemy(app)
	db.create_all()


class User(db.Model):
	__tablename__ = 'ngu_user'

    	uuid = db.Column(db.String(256), primary_key=True)
    	username = db.Column(db.String(256))
    	email = db.Column(db.String(256))

    	def __init__(self, username,emial):
        	self.username = username
        	self.email = email

    	def __repr__(self):
        	return '<User %r>' % self.username

class Picture(db.Model):
	__tablename__ = 'ngu_picture'

    	uuid = db.Column(db.String(256), primary_key=True)
    	path = db.Column(db.String(256))
    	upload_user = db.Column(db.String(256))
	upload_time = db.Column(db.String(256))
	like = db.Column(db.Integer())
	dislike = db.Column(db.Interger)
    	note = db.Column(db.Text)  

    	def __init__(self, path):
        	self.username = username
        	self.email = email

    	def __repr__(self):
        	return '<Picture %r>' % self.username


	
	
