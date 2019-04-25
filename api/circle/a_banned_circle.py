# coding: utf8

from rust.core.business import ParamObject
from rust.core.api import ApiResource, Resource
from rust.core.decorator import param_required
from rust.core.exceptions import BusinessError

from business.circle.ban_service import BanService


@Resource('circle.banned_circle')
class ABannedCircle(ApiResource):
	"""
	禁用的圈子
	"""

	@param_required(['user', 'circle_id'])
	def put(self):
		"""
		禁用圈子(限管理员操作)
		"""
		if not self.params['user'].is_manager:
			raise BusinessError(u'操作无权限')
		user = self.params['user']
		param_object = ParamObject({
			'circle_id': self.params['circle_id']
		})
		BanService(user).ban(param_object)
		return {}

	@param_required(['user', 'circle_id'])
	def delete(self):
		"""
		解禁圈子(限管理员操作)
		"""
		if not self.params['user'].is_manager:
			raise BusinessError(u'操作无权限')
		user = self.params['user']
		param_object = ParamObject({
			'circle_id': self.params['circle_id']
		})
		BanService(user).unban(param_object)
		return {}