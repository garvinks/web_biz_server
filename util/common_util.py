#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Garvin
Email: garvin210905@gmail.com
Created Time: 2024/2/20 14:33
Description: This script is used to do something.
"""
import hashlib
import os
import sys
import time

BASE_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_PATH)

from util.logger_util import logger_info, logger_error


class CommonUtil(object):
    def __init__(self):
        pass

    @staticmethod
    def file_exist(file_path: str) -> bool:
        return os.path.exists(file_path)

    @staticmethod
    def str_to_md5(s: str) -> str:
        md5 = hashlib.md5()
        md5.update(s.encode('utf-8'))
        return md5.hexdigest()
