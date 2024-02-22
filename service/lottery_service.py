#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Garvin
Email: garvin210905@gmail.com
Created Time: 2024/2/22 9:42
Description: This script is used to do something.
"""

import os
import sys

BASE_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_PATH)

from util.logger_util import logger_info, logger_error
from util.sqlite_util import class_sqlite_util


class LotteryService(object):
    def __init__(self):
        pass

    def double_color_ball_buy_ticket(self, red_balls: list, blue_ball: int):
        """
        购买成功 返回唯一追踪号 兑奖日期 增加奖池金额
        :param red_balls:
        :param blue_ball:
        :return:
        """

        pass

    def init_prize(self):

        pass
