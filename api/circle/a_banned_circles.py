#coding: utf8

from rust.core.api import ApiResource, Resource
from rust.core.decorator import param_required
from rust.core.paginator import TargetPage
from rust.core.exceptions import BusinessError

from business.circle.circle_repository import CircleRepository
from business.circle.encode_circle_service import EncodeCircleService

@Resource('circle.banned_circles')
class ABannedCircles(ApiResource):
	"""
	禁用的圈子列表(限管理员操作)
	"""
	@param_required(['user', '?page:int', '?count_per_page:int', '?filters:json'])
	def get(self):
		if not self.params['user'].is_manager:
			raise BusinessError(u'操作无权限')
		user = self.params['user']
		target_page = TargetPage(self.params)
		circles = CircleRepository(user).get_banned_circles(
			self.params.get('filters'),
			target_page
		)
		return {
			'circles': [EncodeCircleService(user).encode(circle) for circle in circles],
			'page_info': target_page.to_dict() if target_page else {}
		}