import unittest
import os
import sys

BASE_PATH = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(BASE_PATH)

from util.response_util import ResponseUtil


class MyTestCase(unittest.TestCase):
    def test_something(self):
        rsp = ResponseUtil.success()
        print(rsp)
        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
