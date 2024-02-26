#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Garvin
Email: garvin210905@gmail.com
Created Time: 2024/2/22 15:43
Description: This script is used to do something.
"""
import os
import sys
import time

BASE_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_PATH)

from util.logger_util import logger_error
from util.sqlite_util import class_sqlite_util
from service.lottery_service import LotteryService


class LotteryPrizeInit(object):
    def __init__(self):
        pass

    @staticmethod
    def set_zero_prize() -> bool:
        ok = True
        conn = class_sqlite_util.get_conn()
        cursor = conn.cursor()
        current_time = int(time.time() * 1000)
        try:
            # 开始事务
            cursor.execute('BEGIN TRANSACTION')
            # 执行SQL命令
            curr_order_no = 'DCB0000000000'  # DCB2024020101
            df = class_sqlite_util.query_df(f"select * from t_lottery_prize where order_no = '{curr_order_no}'")
            if df.shape[0] == 1:
                return ok
            (red_balls, blue_ball, m, s) = LotteryService.gen_random_prize_code()
            order_date = LotteryService.get_prize_date()
            expired_at = LotteryService.get_expire_timestamp(order_date)
            zero_data = (curr_order_no, s, 0, current_time, expired_at, order_date)
            cursor.execute(
                f"insert into t_lottery_prize (order_no, prize_code, prize_pool, created_at, expired_at, order_date) values (?,?,?,?,?,?)",
                zero_data)
            order_no = f"DCB{order_date.replace('-', '')}"
            new_data = (order_no, s, 0, current_time, expired_at, order_date)
            cursor.execute(
                f"insert into t_lottery_prize (order_no, prize_code, prize_pool, created_at, expired_at, order_date) values (?,?,?,?,?,?)",
                new_data)
            # 提交事务
            conn.commit()
        except Exception as e:
            logger_error.error(e)
            ok = False
            conn.rollback()
        finally:
            cursor.close()
        return ok
