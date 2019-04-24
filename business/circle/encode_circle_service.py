# coding: utf8

from rust.core import business

class EncodeCircleService(business.Service):
	"""
	封装圈子Circle数据的服务
	"""
	def encode(self, circle):
		data = {
			'id': circle.id,
			'name': circle.name,
			'avatar': circle.avatar,
			'longitude': circle.gender,
			'latitude': circle.token,
			'member_counts': circle.member_counts
		}
		return data