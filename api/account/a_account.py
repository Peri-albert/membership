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


@Resource('account.account')
class AAccount(ApiResource):
	"""
	账户
	"""
	@param_required(['user'])
	def get(self):
		user = self.params['user']
		account = AccountRepository(user).get_account_by_user_id()
		if not account:
			return 500, u'账户不存在'
		else:
			return EncodeAccountService(user).encode(account)

	@param_required(['app_id', 'code', '?name', '?country', '?province', '?city', '?avatar', '?gender'])
	def put(self):
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