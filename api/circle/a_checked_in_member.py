# coding: utf8

from rust.core.business import ParamObject
from rust.core.api import ApiResource, Resource
from rust.core.decorator import param_required

from business.account.account_repository import AccountRepository
from business.circle.check_in_service import CheckInService


@Resource('circle.checked_in_member')
class ACheckedInMember(ApiResource):
	"""
	签到的成员
	"""
	@param_required(['user', 'circle_id'])
	def put(self):
		"""
		圈子签到
		"""
		user = self.params['user']
		account = AccountRepository(user).get_account_by_user_id()
		param_object = ParamObject({
			'account_id': account.id,
			'circle_id': self.params['circle_id']
		})
		CheckInService(user).check_in(param_object)
		return {}