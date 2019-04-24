# coding: utf8

from rust.core.business import ParamObject
from rust.core.api import ApiResource, Resource
from rust.core.decorator import param_required

from business.account.account_repository import AccountRepository
from business.account.check_in_service import CheckInService


@Resource('account.checked_in_account')
class ACheckedInAccount(ApiResource):
	"""
	签到的用户
	"""
	@param_required(['user'])
	def put(self):
		"""
		用户签到
		"""
		user = self.params['user']
		account = AccountRepository(user).get_account_by_user_id()
		param_object = ParamObject({
			'account_id': account.id
		})
		CheckInService(user).check_in(param_object)
		return {}