import unittest
import os
import sys
import time

BASE_PATH = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(BASE_PATH)

from util.filter_util import class_filter_util


class MyTestCase(unittest.TestCase):
    def test_something(self):
        for i in range(6):
            class_filter_util.filter_by_str("123.1.1.1")
            time.sleep(0.5)
        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
