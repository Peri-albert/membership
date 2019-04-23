# coding: utf8

from rust.core.api import ApiResource, Resource
from rust.core.decorator import param_required

from business.account.encode_account_service import EncodeAccountService
from business.circle.circle_repository import CircleRepository
from business.account.account_repository import AccountRepository

@Resource('circle.members')
class ACircleMembers(ApiResource):
	"""
	圈子成员
	"""
	@param_required(['user', 'circle_id'])
	def get(self):
		user = self.params['user']
		account = AccountRepository.get_account_by_user_id(user.id)
		circle = CircleRepository(user).get_circle_by_id(self.params['circle_id'])
		if not circle:
			return 500, u'圈子不存在'
		else:
			account_ids = circle.get_member_account_ids(circle.id)
			if account.id not in account_ids:
				return 500, u'成员不存在'
			return EncodeAccountService(user).encode(account)