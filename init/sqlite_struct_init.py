#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Garvin
Email: garvin210905@gmail.com
Created Time: 2024/2/21 14:09
Description: This script is used to do something.
"""
import os
import sys

BASE_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_PATH)
RESOURCE_PATH = os.path.join(BASE_PATH, "resource")
SQL_PATH = os.path.join(RESOURCE_PATH, "sql")
INIT_SQL_PATH = os.path.join(SQL_PATH, "init.sql")

from util.sqlite_util import class_sqlite_util
from util.logger_util import logger_info, logger_error


class SqliteStructInit(object):
    def __init__(self):
        pass

    @staticmethod
    def execute_init() -> bool:
        ok = True
        with open(INIT_SQL_PATH, 'r', encoding='utf-8') as file:
            sql_script = file.read()
        logger_info.debug(sql_script)
        conn = class_sqlite_util.get_conn()
        cursor = conn.cursor()
        try:
            # 开始事务
            cursor.execute('BEGIN TRANSACTION')
            # 执行SQL命令
            cursor.executescript(sql_script)
            # 提交事务
            conn.commit()
        except Exception as e:
            logger_error.error(e)
            ok = False
            conn.rollback()
        finally:
            cursor.close()
            conn.close()
        return ok
