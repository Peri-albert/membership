# coding: utf8

import requests
import json
import settings

from rust.core.business import ParamObject
from rust.core.api import ApiResource, Resource
from rust.core.decorator import param_required
from rust.core.exceptions import BusinessError

from business.account.account_repository import AccountRepository
from business.account.account_factory import AccountFactory
from business.account.encode_account_service import EncodeAccountService
from business.account.fill_account_service import FillAccountService


@Resource('account.account')
class AAccount(ApiResource):
	"""
	账户
	"""
	@param_required(['user', '?id', '?with_options:json'])
	def get(self):
		"""
		根据账户id获取账户，否则根据rust用户token登录机制获取自身账户
		"""
		user = self.params['user']
		if self.params.get('id'):
			id = self.params['id']
			account = AccountRepository(user).get_account_by_id(id)
		else:
			account = AccountRepository(user).get_account_by_user_id()

		fill_option = self.params.get('with_options', {'with_status': False})
		FillAccountService(user).fill([account], fill_option)
		return EncodeAccountService(user).encode(account)

	@param_required(['app_id', 'code', '?name', '?country', '?province', '?city', '?avatar', '?gender'])
	def put(self):
		"""
		依据微信小程序创建账户
		"""
		app_id = self.params['app_id']
		app_secret = settings.APPID2SECRET[app_id]
		code = self.params['code']
		wx_req = ParamObject({
			'appid': app_id,
			'secret': app_secret,
			'js_code': code,
			'grant_type': 'authorization_code'
		})
		url = 'https://api.weixin.qq.com/sns/jscode2session'
		res = requests.get(url, params=wx_req)
		res_data = json.loads(res.text)

		basic_info = ParamObject({
			'name': self.params['name'],
			'country': self.params['country'],
			'province': self.params['province'],
			'city': self.params['city'],
			'avatar': self.params['avatar'],
			'gender': self.params['gender'],
			'openid': res_data['openid']
		})
		try:
			account = AccountFactory().create(basic_info)
			account.bind_user()
		except BusinessError:
			account = AccountRepository().get_account_by_openid(res_data['openid'])

		return {
			'id': account.id,
			'token': account.token
		}

	@param_required(['user', '?name', '?country', '?province', '?city', '?avatar', '?gender', '?birthday', '?age'])
	def post(self):
		"""
		修改账户
		"""
		user = self.params['user']
		param_object = ParamObject({
			'name': self.params.get('name'),
			'country': self.params.get('country'),
			'province': self.params.get('province'),
			'city': self.params.get('city'),
			'avatar': self.params.get('avatar'),
			'gender': self.params.get('gender'),
			'birthday': self.params.get('birthday'),
			'age': self.params.get('age'),
		})
		AccountFactory(user).update(param_object)
		return {}
