# coding: utf8

from rust.core.business import ParamObject
from rust.core.api import ApiResource, Resource
from rust.core.decorator import param_required

from business.circle.calculate_distance_service import CalculateDistanceService
from business.circle.circle_repository import CircleRepository


@Resource('circle.circle_distance')
class ACircle(ApiResource):
	"""
	圈子距离
	"""
	@param_required(['user', 'id:int', 'longitude:float', 'latitude:float'])
	def get(self):
		"""
		获取圈子距离
		"""
		user = self.params['user']
		account_longitude = self.params['longitude']
		account_latitude = self.params['latitude']
		circle = CircleRepository(user).get_circle_by_id(self.params['id'])
		circle_longitude = circle.longitude
		circle_latitude = circle.latitude

		param_object = ParamObject({
			'account_longitude': account_longitude,
			'account_latitude': account_latitude,
			'circle_longitude': circle_longitude,
			'circle_latitude': circle_latitude
		})
		distance = CalculateDistanceService(user).get_distance(param_object)
		return distance
