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

from util.logger_util import logger_split
from util.logger_util import logger_common

logger_info = logger_split(log_name="web_biz_server.log")
logger_error = logger_common(log_name="error.log")


class Filter(object):
    def __init__(self):
        self.map = dict()
        self.key_ip = "ip"
        self.map[self.key_ip] = dict()

    def filter_ip(self, ip: str) -> bool:
        current_time = int(time.time())
        val_ip = self.map.get(self.key_ip, dict()).get(ip, list())
        in_time_ip = []
        for i in val_ip:
            if current_time - i > 60:
                continue
            in_time_ip.append(i)
        if len(in_time_ip) > 10:
            logger_error.debug(f"error - {ip} - {in_time_ip}")
            return False
        in_time_ip.append(current_time)
        self.map[self.key_ip][ip] = in_time_ip
        logger_info.debug(f"success - {ip} - {in_time_ip}")
        return True


class_filter = Filter()