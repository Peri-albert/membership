# coding: utf8

from rust.core import db as models


class Circle(models.Model):
	"""
	圈子
	"""
	name = models.CharField(default='', max_length=128) # 姓名
	avatar = models.TextField(default='')  # 头像
	created_at = models.DateTimeField(auto_now_add=True) # 创建时间
	longitude = models.FloatField(default=0) # 经度
	latitude = models.FloatField(default=0) # 纬度
	is_banned = models.BooleanField(default=False) # 禁用情况

	class Meta(object):
		table_name = 'circle_circle'


class CircleMember(models.Model):
	"""
	圈子成员
	"""
	created_at = models.DateTimeField(auto_now_add=True) # 创建时间
	account_id = models.IntegerField(default=0, index=True) # 账户id
	circle_id = models.IntegerField(default=0, index=True) # 圈子id
	is_checked_in = models.BooleanField(default=False)  # 打卡情况

	class Meta(object):
		table_name = 'circle_member'

