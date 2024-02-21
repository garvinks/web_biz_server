import unittest
import os
import sys

BASE_PATH = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(BASE_PATH)

from init.sqlite_struct_init import SqliteStructInit


class MyTestCase(unittest.TestCase):
    def test_something(self):
        ok = SqliteStructInit.execute_init()
        self.assertEqual(True, ok)  # add assertion here


if __name__ == '__main__':
    unittest.main()
