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
from typing import List, Union

import pandas as pd

BASE_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_PATH)
RESOURCE_PATH = os.path.join(BASE_PATH, "resource")
DATA_PATH = os.path.join(RESOURCE_PATH, "data")
SQLITE_DB_PATH = os.path.join(DATA_PATH, "sqlite.db")

from util.logger_util import logger_error, logger_info


class SqliteUtil(object):
    def __init__(self):
        self.conn = sqlite3.connect(SQLITE_DB_PATH)

    def get_conn(self) -> sqlite3.Connection:
        return self.conn

    def close_conn(self) -> None:
        self.conn.close()
        return

    def query(self, sql: str, params: Union[tuple, list] = None) -> List[tuple]:
        cursor = self.get_conn().cursor()
        res = None
        try:
            if params is None:
                cursor.execute(sql)
            else:
                cursor.execute(sql, params)
            res = cursor.fetchall()
        except Exception as e:
            logger_error.error(f"sql:{sql},params:{params},e:{e}")
        finally:
            cursor.close()
        return res

    def query_df(self, sql, params: Union[tuple, list] = None) -> pd.DataFrame:
        df = pd.read_sql(sql, con=self.conn, params=params)
        logger_info.debug(f"shape:{df.shape},columns:{df.columns}")
        return df

    def execute(self, sql: str, params: Union[tuple, list] = None) -> int:
        cursor = self.conn.cursor()
        row = 0
        try:
            if params is None:
                cursor.execute(sql)
            else:
                cursor.execute(sql, params)
            self.conn.commit()
            row = cursor.rowcount
            logger_info.debug(f"affect rows: {row}")
        except Exception as e:
            self.conn.rollback()
            logger_error.error(f"sql:{sql},params:{params},e:{e}")
        finally:
            cursor.close()
        return row

    def execute_many(self, sql, params: List[Union[tuple, list]]) -> int:
        cursor = self.conn.cursor()
        row = 0
        try:
            if params is None:
                cursor.executemany(sql)
            else:
                cursor.executemany(sql, params)
            self.conn.commit()
            row = cursor.rowcount
            logger_info.debug(f"affect rows: {row}")
        except Exception as e:
            self.conn.rollback()
            logger_error.error(f"sql:{sql},params:{params},e:{e}")
        finally:
            cursor.close()
        return row


class_sqlite_util = SqliteUtil()
