# coding: utf8

from rust.core.api import ApiResource, Resource
from rust.core.decorator import param_required
from rust.core.paginator import TargetPage

from business.circle.encode_circle_service import EncodeCircleService
from business.circle.circle_repository import CircleRepository
from business.account.account_repository import AccountRepository


@Resource('account.joined_circles')
class AJoinedCircles(ApiResource):
	"""
	加入的圈子列表
	"""

	@param_required(['user', '?page:int', '?count_per_page:int', '?filters:json'])
	def get(self):
		user = self.params['user']
		filters = self.params.get('filters')
		target_page = TargetPage(self.params)
		account = AccountRepository(user).get_account_by_user_id()
		if not account:
			return 500, u'账户不存在'
		else:
			circle_ids = account.get_joined_circle_ids(account.id)
			filters['id__in'] = circle_ids
			circles = CircleRepository(user).get_circles(filters, target_page)
			return {
				'circles': [EncodeCircleService(user).encode(circle) for circle in circles],
				'page_info': target_page.to_dict() if target_page else {}
			}
