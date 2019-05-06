# coding: utf8

from rust.core.api import ApiResource, Resource
from rust.core.decorator import param_required
from rust.core.paginator import TargetPage

from business.circle.circle_repository import CircleRepository
from business.circle.fill_circle_service import FillCircleService
from business.circle.encode_circle_service import EncodeCircleService


@Resource('circle.circles')
class ACircles(ApiResource):
	"""
	圈子列表
	"""
	@param_required(['user', '?with_options:json', '?page:int', '?count_per_page:int', '?filters:json'])
	def get(self):
		"""
		获取圈子列表
		"""
		user = self.params['user']
		target_page = TargetPage(self.params)
		filters = self.params.get('filters')
		circles = CircleRepository(user).get_circles(filters, target_page)

		fill_option = self.params.get('with_options', {'with_member': False})
		FillCircleService(user).fill(circles, fill_option)

		return {
			'circles': [EncodeCircleService(user).encode(circle) for circle in circles],
			'page_info': target_page.to_dict() if target_page else {}
		}