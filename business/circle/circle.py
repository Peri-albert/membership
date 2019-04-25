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

	@property
	def member_counts(self):
		"""
		成员数量
		"""
		member_counts = circle_models.CircleMember.select().dj_where(circle_id=self.id).count()
		return member_counts