# coding: utf8

from rust.core import business
from rust.resources.business.user.login_service import LoginService as UserLoginService
from rust.resources.db.user import models as user_models

from db.account import models as account_models

class Account(business.Model):
	"""
	账户
	"""
	__slots__ = (
		'id',
		'name',
		'created_at',
		'birthday',
		'age',
		'city',
		'province',
		'country',
		'avatar'
	)

	@property
	def token(self):
		user = UserLoginService().login(self.openid, self.openid[:8])
		return user['token']

	@property
	def user_id(self):
		return self.context['db_model'].user_id

	@property
	def openid(self):
		return self.context['db_model'].openid

	@property
	def gender(self):
		return account_models.GENDER2TEXT[self.context['db_model'].gender]

	def __init__(self, db_model=None):
		super(Account, self).__init__(db_model)

	def bind_user(self):
		"""
		绑定rust的user
		"""
		db_model = user_models.User.create(
			username = self.openid,
			password = self.openid[:8]
		)
		account_models.Account.update(
			user_id = db_model.id
		).dj_where(id=self.id).execute()
