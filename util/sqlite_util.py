#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Garvin
Email: garvin210905@gmail.com
Created Time: 2024/2/20 18:13
Description: This script is used to do something.
"""

import os
import sys
import sqlite3

BASE_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_PATH)
RESOURCE_PATH = os.path.join(BASE_PATH, "resource")
DATA_PATH = os.path.join(RESOURCE_PATH, "data")
SQLITE_DB_PATH = os.path.join(DATA_PATH, "sqlite.db")


class SqliteUtil(object):
    def __init__(self):
        self.conn = sqlite3.connect(SQLITE_DB_PATH)
        self.conn.is_connected()

    def get_conn(self):
        # 事务需要
        return self.conn

    # connection_prod = mysql_object_prod.get_connection()
    # try:
    #     with connection_prod.cursor() as cursor_prod:
    #         # 开启事务
    #         connection_prod.begin()
    #
    #     # 提交事务
    #     logger.info("开始提交事务")
    #     connection_prod.commit()
    # except Exception as e:
    #     # 如果发生异常，回滚事务
    #     connection_prod.rollback()
    #     logger.error("Transaction rolled back due to error:", str(e))
    #
    # finally:
    #     # 关闭数据库连接
    #     connection_prod.close()

    def init_table(self):
        # 游标
        c = self.conn.cursor()

        # 建表语句
        c.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INT,
            name VARCHAR(50),
            age INT
            )""")
        # c.rowcount

        # 执行
        self.conn.commit()

        # 关闭连接
        # self.conn.close()
# c = conn.cursor()
# c.execute('''CREATE TABLE COMPANY
#        (ID INT PRIMARY KEY     NOT NULL,
#        NAME           TEXT    NOT NULL,
#        AGE            INT     NOT NULL,
#        ADDRESS        CHAR(50),
#        SALARY         REAL);''')
# print ("数据表创建成功")
# conn.commit()
# conn.close()
