#coding: utf8

from rust.core import business
from rust.core.exceptions import BusinessError

from business.circle.circle import Circle
from db.circle import models as circle_models

class CircleFactory(business.Service):
	"""
	圈子工厂
	"""
	def create(self, param_object):
		if circle_models.Circle.select().dj_where(name=param_object.name).first():
			raise BusinessError('existed')

		db_model = circle_models.Circle.create(
			name = param_object.name,
			avatar = param_object.avatar,
			longitude = param_object.longitude,
			latitude = param_object.latitude
		)

		return Circle(db_model)

	def update(self, param_object):
		db_model = circle_models.Circle.select().dj_where(id=param_object.id).first()
		modified = False
		if param_object.name is not None and db_model.name != param_object.name:
			db_model.name = param_object.name
			modified = True

		if param_object.avatar is not None and db_model.avatar != param_object.avatar:
			db_model.avatar = param_object.avatar
			modified = True

		if param_object.longitude is not None and db_model.longitude != param_object.longitude:
			db_model.longitude = param_object.longitude
			modified = True

		if param_object.latitude is not None and db_model.latitude != param_object.latitude:
			db_model.latitude = param_object.latitude
			modified = True

		modified and db_model.save()

