# coding: utf8

from rust.core import business

class EncodeAccountService(business.Service):
	"""
	封装账户Account数据的服务
	"""
	def encode(self, account):
		data = {
			'id': account.id,
			'name': account.name,
			'birthday': account.birthday,
			'age': account.age,
			'city': account.city,
			'province': account.province,
			'country': account.country,
			'avatar': account.avatar,
			'gender': account.gender,
			'token': account.token
		}

		if account.status:
			data['status'] = []
			data['status'].append({
				'is_checked_in': account.status.is_checked_in,
				'duration': account.status.duration
			})

		return data