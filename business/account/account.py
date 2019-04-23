#coding: utf8

from rust.core import business
from rust.core.exceptions import BusinessError
from rust.resources.business.user.login_service import LoginService as UserLoginService
from rust.resources.db.user import models as user_models

from db.account import models as account_models
from db.circle import models as circle_models

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

	def get_joined_circle_ids(self, account_id):
		"""
		获取加入的圈子列表
		"""
		db_models = circle_models.CircleMember.select().dj_where(account_id=account_id)
		circle_ids = []
		for db_model in db_models:
			circle_ids.append(db_model.circle_id)
		return circle_ids

	def join_circle(self, param_object):
		"""
		加入圈子
		"""
		if circle_models.CircleMember.select().dj_where(
				account_id=param_object.account_id,
				circle_id=param_object.circle_id
			).exists():
			raise BusinessError('existed')
		else:
			circle_models.CircleMember.create(
				account_id=param_object.account_id,
				circle_id=param_object.circle_id
			)
	def check_in_circle(self, param_object):
		"""
		圈子签到
		"""
		db_model = circle_models.CircleMember.select().dj_where(
			account_id=param_object.account_id,
			circle_id=param_object.circle_id
		).first()
		if not db_model.is_checked_in:
			db_model.is_checked_in = True
			db_model.save()
		else:
			raise BusinessError('already_checked_in')

	def exit_circle(self, param_object):
		"""
		退出圈子
		"""
		circle_models.CircleMember.delete().dj_where(
			account_id=param_object.account_id,
			circle_id=param_object.circle_id
		).execute()

	def check_in(self):
		"""
		签到
		"""
		db_model = account_models.AccountStatus.select().dj_where(
			account_id=self.id
		).first()
		if not db_model.status:
			db_model.is_checked_in = True
			db_model.save()
		else:
			raise BusinessError('already_checked_in')