# -*- coding: utf-8 -*-

from rust.command.base_command import BaseCommand

from db.circle import models as circle_models
from db.account import models as account_models


class Command(BaseCommand):
	help = ''
	args = ''

	def handle(self, *args, **options):
		"""
		每日初始化签到信息
		"""
		print('#' * 80)
		print('daily_init_check_in_info start')
		print('#' * 80)

		print('-*-' * 20)

		account_models.AccountStatus.update(is_checked_in=False).execute()
		print('$' * 80)
		print('account_check_in_info init done')
		print('$' * 80)
		circle_models.CircleMember.update(is_checked_in=False).execute()
		print('$' * 80)
		print('circle_check_in_info init done')
		print('$' * 80)

		print('-*-' * 20)

		print('#' * 80)
		print('daily_init_check_in_info done')
		print('#' * 80)
