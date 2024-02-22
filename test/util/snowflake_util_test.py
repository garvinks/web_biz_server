import unittest
import os
import sys

BASE_PATH = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(BASE_PATH)

from util.snowflake_util import class_snowflake_util


class MyTestCase(unittest.TestCase):
    def test_something(self):
        for _ in range(10):
            print(class_snowflake_util.get_id())
        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
