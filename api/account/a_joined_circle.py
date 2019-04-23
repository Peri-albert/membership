# coding: utf8

from rust.core.business import ParamObject
from rust.core.api import ApiResource, Resource
from rust.core.decorator import param_required

from business.account.account_repository import AccountRepository


@Resource('account.joined_circle')
class AJoinedCircle(ApiResource):
	"""
	加入的圈子
	"""

	@param_required(['user', 'circle_id'])
	def put(self):
		user = self.params['user']
		account = AccountRepository(user).get_account_by_user_id()
		param_object = ParamObject({
			'account_id': account.id,
			'circle_id': self.params['circle_id']
		})
		account.join_circle(param_object)
		return{}

	@param_required(['user', 'circle_id'])
	def post(self):
		user = self.params['user']
		account = AccountRepository(user).get_account_by_user_id()
		param_object = ParamObject({
			'account_id': account.id,
			'circle_id': self.params['circle_id']
		})
		account.check_in_circle(param_object)
		return {}

	@param_required(['user', 'circle_id'])
	def delete(self):
		user = self.params['user']
		account = AccountRepository(user).get_account_by_user_id()
		param_object = ParamObject({
			'account_id': account.id,
			'circle_id': self.params['circle_id']
		})
		account.exit_circle(param_object)
		return {}