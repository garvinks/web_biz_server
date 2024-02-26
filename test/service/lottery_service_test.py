import unittest
import os
import sys

BASE_PATH = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(BASE_PATH)

from service.lottery_service import class_lottery_service


class MyTestCase(unittest.TestCase):
    def test_something(self):
        class_lottery_service.lock = True
        print(class_lottery_service.lock)
        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
