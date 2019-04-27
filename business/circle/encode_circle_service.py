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
			'longitude': circle.longitude,
			'latitude': circle.latitude,
			'members': [],
			'member_amount': 0
		}

		if circle.members:
			data['member_amount'] = circle.member_amount
			for member in circle.members:
				data['members'].append({
					'id': member.id,
					'name': member.name,
					'birthday': member.birthday,
					'age': member.age,
					'city': member.city,
					'province': member.province,
					'country': member.country,
					'avatar': member.avatar,
					'gender': member.gender,
				})
		return data