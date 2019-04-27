# -*- coding: utf-8 -*-

from rust.core import business

from business.account.account import Account
from business.circle.join_in_service import JoinInService

from db.circle import models as circle_models
from db.account import models as account_models


class FillCircleService(business.Service):

	def __fill_member_data(self, circles):
		circle_ids = [circle.id for circle in circles]
		record_db_models = circle_models.CircleMember.select().dj_where(circle_id__in=circle_ids)
		account_ids = [record_db_model.account_id for record_db_model in record_db_models]
		db_models = account_models.Account.select().dj_where(id__in=account_ids)
		account_id2account = {db_model.id: Account(db_model) for db_model in db_models}
		for circle in circles:
			circle.members = []
			member_ids = JoinInService(self.user).get_serial_member_ids(circle.id)
			for member_id in member_ids:
				circle.members.append(account_id2account[member_id])

			circle.member_amount = len(circle.members)

	def fill(self, circles, options=None):
		options = options or {}
		if options.get('with_member', False):
			self.__fill_member_data(circles)
