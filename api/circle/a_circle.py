# coding: utf8

from rust.core.business import ParamObject
from rust.core.api import ApiResource, Resource
from rust.core.decorator import param_required
from rust.core.exceptions import BusinessError

from business.circle.circle_repository import CircleRepository
from business.circle.circle_factory import CircleFactory
from business.circle.encode_circle_service import EncodeCircleService


@Resource('circle.circle')
class ACircle(ApiResource):
	"""
	圈子
	"""
	@param_required(['user', 'id:int'])
	def get(self):
		"""
		获取圈子详情
		"""
		user = self.params['user']
		circle = CircleRepository(user).get_circle_by_id(self.params['id'])

		return EncodeCircleService(user).encode(circle)

	@param_required(['user', 'name', 'avatar', '?longitude', '?latitude'])
	def put(self):
		"""
		创建圈子(限管理员操作)
		"""
		if not self.params['user'].is_manager:
			raise BusinessError(u'操作无权限')
		user = self.params['user']
		param_object = ParamObject({
			'name': self.params['name'],
			'avatar': self.params['avatar'],
			'longitude': self.params.get('longitude'),
			'latitude': self.params.get('latitude')
		})
		circle = CircleFactory(user).create(param_object)
		return {
			'id': circle.id
		}

	@param_required(['user', 'id:int', '?name', '?avatar', '?longitude', '?latitude'])
	def post(self):
		"""
		更新圈子(限管理员操作)
		"""
		if not self.params['user'].is_manager:
			raise BusinessError(u'操作无权限')
		user = self.params['user']
		param_object = ParamObject({
			'id': self.params['id'],
			'name': self.params.get('name'),
			'avatar': self.params.get('avatar'),
			'longitude': self.params.get('longitude'),
			'latitude': self.params.get('latitude')
		})
		CircleFactory(user).update(param_object)
		return {}
