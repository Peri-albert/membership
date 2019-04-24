# coding: utf8

from rust.core.api import ApiResource, Resource
from rust.core.decorator import param_required
from rust.core.paginator import TargetPage

from business.account.encode_account_service import EncodeAccountService
from business.circle.circle_repository import CircleRepository
from business.account.account_repository import AccountRepository


@Resource('circle.members')
class ACircleMembers(ApiResource):
	"""
	圈子成员列表
	"""
	@param_required(['user', 'circle_id', '?page:int', '?count_per_page:int', '?filters:json'])
	def get(self):
		"""
		获取圈子成员列表
		"""
		user = self.params['user']
		filters = self.params.get('filters')
		target_page = TargetPage(self.params)
		circle = CircleRepository(user).get_circle_by_id(self.params['circle_id'])
		if not circle:
			return 500, u'圈子不存在'
		else:
			accounts = AccountRepository(user).get_accounts_by_circle_id(circle.id, filters, target_page)
			return {
				'accounts': [EncodeAccountService(user).encode(account) for account in accounts],
				'page_info': target_page.to_dict() if target_page else {}
			}