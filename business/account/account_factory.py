# coding: utf8

from rust.core import business
from rust.core.exceptions import BusinessError

from business.account.account import Account
from db.account import models as account_models

class AccountFactory(business.Service):
	"""
	账户工厂
	"""
	def create(self, param_object):
		"""
		创建Account对象
		"""
		if account_models.Account.select().dj_where(openid=param_object.openid).exists():
			raise BusinessError('existed')
		else:
			db_model = account_models.Account.create(
				name = param_object.name,
				country = param_object.country,
				province = param_object.province,
				city = param_object.city,
				avatar = param_object.avatar,
				gender = account_models.GENDER[param_object.gender.upper()],
				openid = param_object.openid
			)
		return Account(db_model)

	def update(self, param_object):
		"""
		更新account对象
		"""
		db_model = account_models.Account.select().dj_where(user_id=self.user.id).first()
		modified = False
		if param_object.name is not None and db_model.name != param_object.name:
			db_model.name = param_object.name
			modified = True

		if param_object.country is not None and db_model.country != param_object.country:
			db_model.country = param_object.country
			modified = True

		if param_object.province is not None and db_model.province != param_object.province:
			db_model.province = param_object.province
			modified = True

		if param_object.city is not None and db_model.city != param_object.city:
			db_model.city = param_object.city
			modified = True

		if param_object.avatar is not None and db_model.avatar != param_object.avatar:
			db_model.avatar = param_object.avatar
			modified = True

		if param_object.gender is not None and db_model.gender != param_object.gender:
			db_model.gender = param_object.gender
			modified = True

		if param_object.birthday is not None and db_model.birthday != param_object.birthday:
			db_model.birthday = param_object.birthday
			modified = True

		if param_object.age is not None and db_model.age != param_object.age:
			db_model.age = param_object.age
			modified = True

		modified and db_model.save()
