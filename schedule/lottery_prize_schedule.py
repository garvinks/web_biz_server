#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Garvin
Email: garvin210905@gmail.com
Created Time: 2024/2/26 14:11
Description: This script is used to do something.
"""
import os
import sys
from datetime import datetime

BASE_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_PATH)

from util.logger_util import logger_info
from util.sqlite_util import class_sqlite_util
from service.lottery_service import class_lottery_service, LotteryService


def cal_remain_prize(level: int, cnt: int, prize: int) -> int:
    normal_map = {
        '6': 5,
        '5': 10,
        '4': 200,
        '3': 3000,
    }
    if level in (3, 4, 5, 6):
        return prize - normal_map[str(level)] * cnt
    if level == 2 and prize > 0:
        each = prize * 0.25 / cnt
        if each > 5000000:
            return prize - 5000000 * cnt
        return prize - int(prize * 0.25)
    if level == 1 and prize > 0:
        each = prize * 0.75 / cnt
        if each > 5000000:
            return prize - 5000000 * cnt
        return prize - int(prize * 0.75)
    return prize


class LotteryPrizeSchedule:
    def __init__(self):
        pass

    @staticmethod
    def cal_wait_timestamp() -> int:
        prize_time = '21:30:00'
        n = datetime.now()
        today = n.date()
        curr_timestamp = int(n.timestamp() * 1000)
        split_timestamp = int(datetime.strptime(f'{today} {prize_time}', "%Y-%m-%d %H:%M:%S").timestamp() * 1000)
        day_timestamp = 24 * 60 * 60 * 1000
        res = split_timestamp - curr_timestamp
        logger_info.info(f'cal_wait_timestamp: {res}')
        if res > 0:
            return res
        return res + day_timestamp

    @staticmethod
    def refresh_dcb_prize():
        logger_info.debug('定时任务 - 开始刷新双色球')
        n = datetime.now()
        today = n.date()
        weekday = n.weekday()
        if weekday not in (1, 3, 6) or today.strftime('%H:%M:%S') != '21:30:00':
            return
        logger_info.info('开始锁定购买 刷新奖池')
        class_lottery_service.lock = True
        # 计算上期剩余金额
        res = class_sqlite_util.query(
            f"select id,order_no,prize_pool from t_lottery_prize order by id desc limit 1")
        (prize_id, order_no, prize_pool) = res[0]

        prize_df = class_sqlite_util.query_df(
            f"select prize_level,count(*) as cnt from t_lottery_order where prize_id={prize_id} and prize_level!=0 group by prize_level order by prize_level")
        for _, r in prize_df.iterrows():
            prize_level = int(r['prize_level'])
            cnt = int(r['cnt'])
            prize_pool = cal_remain_prize(prize_level, cnt, prize_pool)

        # 构造新的奖池
        tail_order = str(int(order_no[-2:]) + 1)
        if len(tail_order) == 1:
            tail_order = '0' + tail_order
        (red_balls, blue_ball, m, s) = LotteryService.gen_random_prize_code()
        order_date = today.strftime('%Y-%m-%d %H:%M:%S')
        expired_at = LotteryService.get_expire_timestamp(order_date)
        order_no = f"DCB{order_date.replace('-', '')[:-2]}" + tail_order
        curr_timestamp = int(n.timestamp() * 1000)
        new_data = (order_no, s, prize_pool, curr_timestamp, expired_at, order_date)
        class_sqlite_util.execute(
            f"insert into t_lottery_prize (order_no, prize_code, prize_pool, created_at, expired_at, order_date) VALUES (?,?,?,?,?,?)",
            new_data)
        class_sqlite_util.execute(
            f"update t_lottery_prize set prize_code='{s}',prize_pool={prize_pool},created_at={curr_timestamp},expired_at={expired_at},order_date='{order_date}' where id=1")

        # 可以继续购买
        class_lottery_service.lock = False
