# coding: utf8

from math import radians, cos, sin, asin, sqrt

from rust.core import business

EARTH_RADIUS = 6378.137


class CalculateDistanceService(business.Service):
	"""
	圈子距离服务
	"""
	def get_distance(self, param_object):
		"""
		获取圈子距离
		"""
		account_longitude = param_object.account_longitude
		account_latitude = param_object.account_latitude
		circle_longitude = param_object.circle_longitude
		circle_latitude = param_object.circle_latitude

		account_longitude, account_latitude, circle_longitude, circle_latitude = map(
			radians,
			[account_longitude, account_latitude, circle_longitude, circle_latitude]
		)
		distance_longitude = circle_longitude - account_longitude
		distance_latitude = circle_latitude - account_latitude
		angle = sin(distance_latitude / 2) ** 2 + cos(account_latitude) * cos(circle_latitude) * sin(distance_longitude / 2) ** 2
		return 2000 * asin(sqrt(angle)) * EARTH_RADIUS
