# coding: utf8

from rust.core import business

class Status(business.Model):
	"""
	账户状态：签到/未签到
	"""
	__slots__ = (
		'id',
		'is_checked_in'
	)

	@property
	def account_id(self):
		return self.context['db_model'].account_id

	@property
	def duration(self):
		return self.context['db_model'].duration

	def __init__(self, db_model=None):
		super(Status, self).__init__(db_model)