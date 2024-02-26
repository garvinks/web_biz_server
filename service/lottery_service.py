#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Garvin
Email: garvin210905@gmail.com
Created Time: 2024/2/22 9:42
Description: This script is used to do something.
"""
import json
import os
import random
import sys
from typing import Tuple, List
from datetime import datetime, timedelta

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

    @staticmethod
    def gen_random_prize_code() -> Tuple[List[int], int, dict, str]:
        red_balls = []
        for _ in range(6):
            red_balls.append(random.randint(1, 33))
        red_balls = sorted(red_balls)
        blue_ball = random.randint(1, 16)
        m = {'red_balls': red_balls, 'blue_ball': blue_ball}
        s = json.dumps(m)
        return red_balls, blue_ball, m, s

    @staticmethod
    def get_prize_date() -> str:
        prize_time = '21:30:00'
        n = datetime.now()
        weekday = n.weekday()
        today = n.date()
        if weekday in (1, 3, 6):
            curr_timestamp = int(n.timestamp() * 1000)
            split_timestamp = int(datetime.strptime(f'{today} {prize_time}', "%Y-%m-%d %H:%M:%S").timestamp() * 1000)
            if curr_timestamp >= split_timestamp:
                # 用今天初始化期次
                return today.strftime('%Y-%m-%d')
        # 用上次初始化期次
        if weekday == 0:
            return (today - timedelta(days=1)).strftime("%Y-%m-%d")
        if weekday == 1:
            return (today - timedelta(days=2)).strftime("%Y-%m-%d")
        if weekday == 2:
            return (today - timedelta(days=1)).strftime("%Y-%m-%d")
        if weekday == 3:
            return (today - timedelta(days=2)).strftime("%Y-%m-%d")
        if weekday == 4:
            return (today - timedelta(days=1)).strftime("%Y-%m-%d")
        if weekday == 5:
            return (today - timedelta(days=2)).strftime("%Y-%m-%d")
        if weekday == 6:
            return (today - timedelta(days=3)).strftime("%Y-%m-%d")

    @staticmethod
    def get_expire_timestamp(date: str) -> int:
        return int((datetime.strptime(date + " 21:30:00", "%Y-%m-%d %H:%M:%S") + timedelta(days=60)).timestamp() * 1000)
