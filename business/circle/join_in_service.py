# coding: utf8

from rust.core import business
from rust.core.exceptions import BusinessError

from db.circle import models as circle_models


class JoinInService(business.Service):
	"""
	加入圈子服务
	"""
	def join(self, param_object):
		"""
		加入圈子
		"""
		if circle_models.CircleMember.select().dj_where(
				account_id=param_object.account_id,
				circle_id=param_object.circle_id
		).exists():
			raise BusinessError('existed')
		else:
			circle_models.CircleMember.create(
				account_id=param_object.account_id,
				circle_id=param_object.circle_id
			)

	def exit(self, param_object):
		"""
		退出圈子
		"""
		circle_models.CircleMember.delete().dj_where(
			account_id=param_object.account_id,
			circle_id=param_object.circle_id
		).execute()
