#coding: utf8

from rust.core import business

from business.account.account import Account

from db.account import models as account_models
from db.circle import models as circle_models

class AccountRepository(business.Service):
	"""
	获取Account对象的repository
	"""
	def get_account_by_id(self, account_id):
		"""
		根据id获取account对象
		"""
		db_model = account_models.Account.select().dj_where(id=account_id).first()
		if db_model:
			return Account(db_model)

	def get_account_by_openid(self, openid):
		"""
		根据openid获取account对象
		"""
		db_model = account_models.Account.select().dj_where(openid=openid).first()
		if db_model:
			return Account(db_model)

	def get_account_by_user_id(self):
		"""
		根据user_id获取account对象
		"""
		db_model = account_models.Account.select().dj_where(user_id=self.user.id).first()
		if db_model:
			return Account(db_model)

	def get_accounts(self, filters=None, target_page=None):
		"""
		获取用户列表
		"""
		db_models = account_models.Account.select()
		if filters:
			db_models = db_models.dj_where(**filters)

		if target_page:
			db_models = target_page.paginate(db_models)

		db_models = db_models.order_by(account_models.Account.id.desc())
		return [Account(db_model) for db_model in db_models]

	def get_accounts_by_circle_id(self, circle_id, filters=None, target_page=None):
		"""
		获取成员账户列表
		"""
		db_models = circle_models.CircleMember.select().dj_where(circle_id=circle_id)
		account_ids = []
		for db_model in db_models:
			account_ids.append(db_model.account_id)
		db_models = account_models.Account.select().dj_where(id__in=account_ids)
		if filters:
			db_models = db_models.dj_where(**filters)

		if target_page:
			db_models = target_page.paginate(db_models)

		db_models = db_models.order_by(account_models.Account.id.desc())
		return [Account(db_model) for db_model in db_models]