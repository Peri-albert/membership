#coding: utf8

from rust.core import db as models

GENDER = {
	'UNKNOWN': 0,
	'MALE': 1,
	'FEMALE': 2
}

GENDER2TEXT = {
	GENDER['UNKNOWN']: 'unknown',
	GENDER['MALE']: 'male',
	GENDER['FEMALE']: 'female'
}

class Account(models.Model):
	"""
	账户
	"""
	name = models.CharField(default='', max_length=128) # 姓名
	created_at = models.DateTimeField(auto_now_add=True) # 创建时间
	country = models.CharField(default='', max_length=128) # 国家
	province = models.CharField(default='', max_length=128) # 省份
	city = models.CharField(default='', max_length=128) # 城市
	avatar = models.TextField(default='') # 头像
	gender = models.IntegerField(default=0) # 性别
	birthday = models.DateTimeField(null=True) # 生日
	age = models.IntegerField(default=0) # 年龄
	openid = models.CharField(default='', max_length=255, index=True) # 微信用户的id
	user_id = models.IntegerField(default=0, index=True) # 对应rust的user的id

	class Meta(object):
		table_name = 'account_account'

class AccountStatus(models.Model):
	"""
	账户状态：签到/未签到
	"""
	account_id = models.IntegerField(default=0) # 账户id
	is_checked_in = models.BooleanField(default=False) # 签到情况
	duration = models.IntegerField(default=1) # 持续时长

	class Meta(object):
		table_name = 'account_status'

