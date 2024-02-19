import unittest
import os
import sys
import time

BASE_PATH = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(BASE_PATH)

from service.filter import class_filter


class MyTestCase(unittest.TestCase):
    def test_something(self):
        for i in range(6):
            class_filter.filter_ip("123.1.1.1")
            time.sleep(0.5)
        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
