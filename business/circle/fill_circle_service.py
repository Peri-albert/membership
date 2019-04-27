# -*- coding: utf-8 -*-

from rust.core import business

from business.account.account import Account

from db.circle import models as circle_models
from db.account import models as account_models

class FillCircleService(business.Service):


	def __fill_member_data(self, circles):
		id2circle = {circle.id: circle for circle in circles}

		circle_ids = [circle.id for circle in circles]
		record_db_models = circle_models.CircleMember.select().dj_where(circle_id__in=circle_ids).order_by('id')

		join_order = {}
		for record_db_model in record_db_models:
			join_order.setdefault(record_db_model.circle_id, []).append(record_db_model.account_id)

		account_ids = [record_db_model.account_id for record_db_model in record_db_models]
		db_models = account_models.Account.select().dj_where(id__in=account_ids)
		account_id2account = {db_model.id: Account(db_model) for db_model in db_models}
		for circle in circles:
			circle.members = []
			serial_account_ids = join_order.setdefault(circle.id, [])
			for serial_account_id in serial_account_ids:
				circle.members.append(account_id2account[serial_account_id])

			circle.member_amount = len(circle.members)


	def fill(self, circles, options=None):
		options = options or {}
		if options.get('with_member', False):
			self.__fill_member_data(circles)