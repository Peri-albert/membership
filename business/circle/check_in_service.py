# coding: utf8

from rust.core import business
from rust.core.exceptions import BusinessError

from db.circle import models as circle_models


class CheckInService(business.Service):
	"""
	圈子签到服务
	"""
	def check_in(self, param_object):
		"""
		圈子签到
		"""
		if circle_models.CircleMember.select().dj_where(
			account_id=param_object.account_id,
			circle_id=param_object.circle_id
		).exists():
			db_model = circle_models.CircleMember.select().dj_where(
				account_id=param_object.account_id,
				circle_id=param_object.circle_id
			).first()
			if not db_model.is_checked_in:
				db_model.is_checked_in = True
				db_model.save()
			else:
				raise BusinessError('already_checked_in')
		else:
			raise BusinessError('not_join_in')