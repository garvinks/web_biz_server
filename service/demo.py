#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Garvin
Email: garvin210905@gmail.com
Created Time: 2024/2/19 14:57
Description: This script is used to do something.
"""

import os
import sys

BASE_PATH = os.path.join(os.path.dirname(__file__))
sys.path.append(BASE_PATH)

from util.logger_util import logger_split
from util.logger_util import logger_common

logger_info = logger_split(log_name="web_biz_server.log")
logger_error = logger_common(log_name="error.log")


def main():
    logger_info.info("main")
    logger_error.info("main")


if __name__ == "__main__":
    main()
