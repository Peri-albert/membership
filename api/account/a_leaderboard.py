# coding: utf8

from rust.core.api import ApiResource, Resource
from rust.core.decorator import param_required
from rust.core.paginator import TargetPage

from business.account.account_repository import AccountRepository
from business.account.encode_account_service import EncodeAccountService


@Resource('account.leaderboard')
class ALeaderboard(ApiResource):
	"""
	排行榜
	"""
	@param_required(['user', '?page:int', '?count_per_page:int', '?filters:json'])
	def get(self):
		"""
		获取加入的圈子列表
		"""
		user = self.params['user']
		filters = self.params.get('filters')
		target_page = TargetPage(self.params)
		accounts = AccountRepository(user).get_accounts_in_leaderboard(filters, target_page)
		return {
			'accounts': [EncodeAccountService(user).encode(account) for account in accounts],
			'page_info': target_page.to_dict() if target_page else {}
		}