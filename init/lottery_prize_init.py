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

BASE_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_PATH)

from util.logger_util import logger_error
from util.sqlite_util import class_sqlite_util


class LotteryPrizeInit(object):
    def __init__(self):
        pass

    @staticmethod
    def set_zero_prize() -> bool:
        ok = True
        conn = class_sqlite_util.get_conn()
        cursor = conn.cursor()
        try:
            # 开始事务
            cursor.execute('BEGIN TRANSACTION')
            # 执行SQL命令
            # cursor.executescript(sql_script)
            # 提交事务
            conn.commit()
        except Exception as e:
            logger_error.error(e)
            ok = False
            conn.rollback()
        finally:
            cursor.close()
        return ok
