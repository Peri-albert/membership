# coding: utf8

from rust.core import business

from business.circle.circle import Circle

from db.circle import models as circle_models

class CircleRepository(business.Service):
	"""
	获取Circle对象的repository
	"""
	def get_circle_by_id(self, circle_id):
		"""
		根据id获取圈子
		"""
		db_model = circle_models.Circle.select().dj_where(id=circle_id, is_banned=False).first()
		if db_model:
			return Circle(db_model)

	def get_circles(self, filters=None, target_page=None):
		"""
		获取圈子列表
		"""
		db_models = circle_models.Circle.select().dj_where(is_banned=False)
		if filters:
			db_models = db_models.dj_where(**filters)

		if target_page:
			db_models = target_page.paginate(db_models)

		db_models = db_models.order_by('-id')
		return [Circle(db_model) for db_model in db_models]

	def get_banned_circles(self, filters=None, target_page=None):
		"""
		获取被禁用的圈子列表
		"""
		db_models = circle_models.Circle.select().dj_where(is_banned=True)
		if filters:
			db_models = db_models.dj_where(**filters)

		if target_page:
			db_models = target_page.paginate(db_models)

		db_models = db_models.order_by('-id')
		return [Circle(db_model) for db_model in db_models]

	def get_joined_circles_by_account_id(self, account_id, filters=None, target_page=None):
		"""
		根据account的id获取加入的圈子列表
		"""
		db_models = circle_models.CircleMember.select().dj_where(account_id=account_id)
		circle_ids = []
		for db_model in db_models:
			circle_ids.append(db_model.circle_id)

		db_models = circle_models.Circle.select().dj_where(id__in=circle_ids, is_banned=False)
		if filters:
			db_models = db_models.dj_where(**filters)

		if target_page:
			db_models = target_page.paginate(db_models)

		db_models = db_models.order_by('-id')
		return [Circle(db_model) for db_model in db_models]