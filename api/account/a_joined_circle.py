# coding: utf8

from rust.core.business import ParamObject
from rust.core.api import ApiResource, Resource
from rust.core.decorator import param_required

from business.circle.join_in_service import JoinInService
from business.account.account_repository import AccountRepository


@Resource('account.joined_circle')
class AJoinedCircle(ApiResource):
	"""
	加入的圈子
	"""
	@param_required(['user', 'circle_id'])
	def put(self):
		"""
		加入圈子
		"""
		user = self.params['user']
		account = AccountRepository(user).get_account_by_user_id()
		param_object = ParamObject({
			'account_id': account.id,
			'circle_id': self.params['circle_id']
		})
		JoinInService(user).join(param_object)
		return{}

	@param_required(['user', 'circle_id'])
	def delete(self):
		"""
		退出圈子
		"""
		user = self.params['user']
		account = AccountRepository(user).get_account_by_user_id()
		param_object = ParamObject({
			'account_id': account.id,
			'circle_id': self.params['circle_id']
		})
		JoinInService(user).exit(param_object)
		return {}