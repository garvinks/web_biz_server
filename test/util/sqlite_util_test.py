import unittest
import os
import sys
import time

BASE_PATH = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(BASE_PATH)

from util.sqlite_util import class_sqlite_util


class MyTestCase(unittest.TestCase):
    def test_something(self):
        time_stamp = int(time.time() * 1000)
        d = ('garvin', 'admin', time_stamp, time_stamp)
        sql = "insert into t_user (name,remark,created_at,updated_at) values (?, ?, ?, ?)"
        row = class_sqlite_util.execute(sql, d)
        print(row)
        self.assertEqual(True, True)  # add assertion here

    def test_something_else(self):
        sql = "select * from t_user where id=?"
        a = class_sqlite_util.query_df(sql, (1,))
        print(a)
        self.assertEqual(True, True)  # add assertion here

    def test_something_else2(self):
        sql = "select * from t_user where id=?"
        a = class_sqlite_util.query(sql, (1,))
        print(a)
        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
