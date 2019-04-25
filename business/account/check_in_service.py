# coding: utf8

from rust.core import business
from rust.core.exceptions import BusinessError

from db.account import models as account_models

class CheckInService(business.Service):
	"""
	账户签到服务
	"""
	def check_in(self, param_object):
		"""
		签到
		"""
		if account_models.AccountStatus.select().dj_where(account_id=param_object.account_id).exists():
			db_model = account_models.AccountStatus.select().dj_where(account_id=param_object.account_id).first()
			if not db_model.status:
				db_model.is_checked_in = True
				db_model.duration += 1
				db_model.save()
			else:
				raise BusinessError('already_checked_in')
		else:
			account_models.AccountStatus.create(
				account_id = param_object.account_id,
				is_checked_in = True
			)