# coding: utf8

from rust.core.api import ApiResource, Resource
from rust.core.decorator import param_required

from business.account.account_repository import AccountRepository

@Resource('account.account_status')
class AAccount(ApiResource):
	"""
	账户签到状态
	"""
	@param_required(['user'])
	def put(self):
		user = self.params['user']
		account = AccountRepository(user).get_account_by_user_id()
		if not account:
			return 500, u'账户不存在'
		else:
			account.check_in()