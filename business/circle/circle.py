#coding: utf8

from rust.core import business

from db.circle import models as circle_models

class Circle(business.Model):

	__slots__ = (
		'id',
		'name',
		'created_at',
		'longitude',
		'latitude',
		'is_banned'
	)

	def __init__(self, db_model=None):
		super(Circle, self).__init__(db_model)

	def get_member_account_ids(self, circle_id):
		"""
		获取成员账户列表
		"""
		db_models = circle_models.CircleMember.select().dj_where(circle_id=circle_id)
		account_ids = []
		for db_model in db_models:
			account_ids.append(db_model.account_id)
		return account_ids