import unittest
import os
import sys

BASE_PATH = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(BASE_PATH)

from service.get_ip_region import ip_searcher


class MyTestCase(unittest.TestCase):
    def test_something(self):
        ip_array = [
            "1.2.3.4",
            "192.168.1.1",
            "119.123.79.246",
            "112.97.47.25",
        ]
        # 3. 执行查询
        # ip = "1.2.3.4"
        for ip in ip_array:
            region_str = ip_searcher.searchByIPStr(ip)
            print(region_str)
        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
