#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Garvin
Email: garvin210905@gmail.com
Created Time: 2024/2/19 16:24
Description: This script is used to do something.
"""

import os
import sys
import time

BASE_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_PATH)

from util.logger_util import logger_info, logger_error


class FilterUtil(object):
    def __init__(self):
        self.map = dict()
        self.key_ip = "ip"
        self.map[self.key_ip] = dict()

    def filter_by_str(self, s: str, limit: int = 5, timeout: int = 5) -> bool:
        current_time = int(time.time())
        val_ip = self.map.get(self.key_ip, dict()).get(s, list())
        in_time_ip = []
        for i in val_ip:
            if current_time - i > timeout:
                continue
            in_time_ip.append(i)
        if len(in_time_ip) > limit:
            logger_error.debug(f"error - {s} - {in_time_ip}")
            return False
        in_time_ip.append(current_time)
        self.map[self.key_ip][s] = in_time_ip
        logger_info.debug(f"success - {s} - {in_time_ip}")
        return True


class_filter_util = FilterUtil()
