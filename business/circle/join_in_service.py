# coding: utf8

from rust.core import business
from rust.core.exceptions import BusinessError

from db.circle import models as circle_models

CIRCLE_ID2MEMBERS = {}


class JoinInService(business.Service):
	"""
	加入圈子服务
	"""
	def join(self, param_object):
		"""
		加入圈子
		"""
		global CIRCLE_ID2MEMBERS
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
			CIRCLE_ID2MEMBERS.setdefault(param_object.circle_id, default=[]).append(param_object.account_id)

	def exit(self, param_object):
		"""
		退出圈子
		"""
		global CIRCLE_ID2MEMBERS
		circle_models.CircleMember.delete().dj_where(
			account_id=param_object.account_id,
			circle_id=param_object.circle_id
		).execute()
		if CIRCLE_ID2MEMBERS.setdefault(param_object.circle_id, default=[]).count(param_object.account_id) > 0:
			CIRCLE_ID2MEMBERS[param_object.circle_id].remove(param_object.account_id)

	def get_serial_member_ids(self, param_object):
		"""
		获取按照加入顺序排列的用户id列表
		"""
		global CIRCLE_ID2MEMBERS
		circle_id = param_object.circle_id

		return CIRCLE_ID2MEMBERS.setdefault(circle_id, default=[])

