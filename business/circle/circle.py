# coding: utf8

from rust.core import business

from db.circle import models as circle_models


class Circle(business.Model):
	"""
	圈子
	"""
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
