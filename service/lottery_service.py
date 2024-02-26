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
import time
from typing import Tuple, List
from datetime import datetime, timedelta

BASE_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_PATH)

from util.logger_util import logger_info, logger_error
from util.common_util import CommonUtil
from util.sqlite_util import class_sqlite_util


def claim_balls(red: int, blue: bool) -> int:
    if red == 6 and blue is True:
        return 1
    if red == 6 and blue is False:
        return 2
    if red == 5 and blue is True:
        return 3
    if (red == 5 and blue is False) or (red == 4 and blue is True):
        return 4
    if (red == 4 and blue is False) or (red == 3 and blue is True):
        return 5
    if blue is True and red in (0, 1, 2):
        return 6
    return 0


class LotteryService(object):
    def __init__(self):
        self.lock = False
        self.red_balls = None
        self.blue_ball = None
        self.prize_id = None
        self.order_code = None

    def double_color_ball_buy_ticket(self, red_balls: list, blue_ball: int) -> str:
        """
        购买成功 返回唯一追踪号 兑奖日期 增加奖池金额
        :param red_balls:
        :param blue_ball:
        :return:
        """
        if self.red_balls is None or self.blue_ball is None or self.prize_id is None or self.order_code is None:
            res = class_sqlite_util.query("select id,prize_code,order_no from t_lottery_prize order by id desc limit 1")
            (prize_id, prize_code, order_no) = res[0]
            self.red_balls = json.loads(prize_code)['red_balls']
            self.blue_ball = json.loads(prize_code)['blue_ball']
            self.prize_id = prize_id
            self.order_code = order_no
        i = 0
        j = 0
        s = 0
        while True:
            if i == 6 or j == 6:
                break
            if red_balls[i] > self.red_balls[j]:
                j += 1
                continue
            if red_balls[i] < self.red_balls[j]:
                i += 1
                continue
            i += 1
            j += 1
            s += 1
        x = False
        if blue_ball == self.blue_ball:
            x = True
        level = claim_balls(s, x)
        trace_id = CommonUtil.get_uuid()
        code = {'red_balls': red_balls, 'blue_ball': blue_ball}
        curr_timestamp = int(time.time() * 1000)
        # 加记录 加奖金额
        order = (trace_id, self.prize_id, json.dumps(code), 0, level, curr_timestamp, curr_timestamp)
        class_sqlite_util.execute(
            f"insert into t_lottery_order (trace_id, prize_id, order_code, status, prize_level, created_at, updated_at) VALUES (?,?,?,?,?,?,?)",
            order)
        class_sqlite_util.execute(f"update t_lottery_prize set prize_pool=prize_pool+2 where id in (1,{self.prize_id})")
        return trace_id

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


class_lottery_service = LotteryService()
