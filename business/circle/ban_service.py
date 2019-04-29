# coding: utf8

from rust.core import business

from db.circle import models as circle_models


class BanService(business.Service):
	"""
	禁用圈子服务
	"""
	def ban(self, param_object):
		"""
		禁用圈子
		"""
		circle_models.Circle.update(
			is_banned = True
		).dj_where(id=param_object.circle_id).execute()

	def unban(self, param_object):
		"""
		解禁圈子
		"""
		circle_models.Circle.update(
			is_banned = False
		).dj_where(id=param_object.circle_id).execute()
