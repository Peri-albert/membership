#coding: utf8

from rust.core import business

from business.circle.circle import Circle

from db.circle import models as circle_models

class CircleRepository(business.Service):

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
		db_models = circle_models.Circle.select()
		if filters:
			db_models = db_models.dj_where(**filters)
		else:
			db_models = db_models.dj_where(is_banned=False)

		if target_page:
			db_models = target_page.paginate(db_models)

		db_models = db_models.order_by(circle_models.Circle.id.desc())
		return [Circle(db_model) for db_model in db_models]