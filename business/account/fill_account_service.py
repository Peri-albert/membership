# -*- coding: utf-8 -*-

from rust.core import business

from db.account import models as account_models

from .status import Status

class FillAccountService(business.Service):
	def __fill_status_data(self, accounts):
		id2account = {account.id: account for account in accounts}

		account_ids = [account.id for account in accounts]
		db_models = account_models.AccountStatus.select().dj_where(account_id__in=account_ids)
		for account in accounts:
			account.status = []

		for db_model in db_models:
			id2account.setdefault(db_model.account_id, []).status.append(Status(db_model))

	def fill(self, accounts, options=None):
		options = options or {}
		if options.get('with_status', False):
			self.__fill_status_data(accounts)