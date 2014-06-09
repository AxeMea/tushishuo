#encoding utf-8
from core.share.moel.models import *

#拉取推荐故事
def get_recommand_storys():
	return Story.query.order_by(like)

#拉取精彩评论
def get_good_comments():
	return Comment.query.order_by(like) 

#最新主题
def get_index_themes():
	return Theme.query.limit(3).all()
