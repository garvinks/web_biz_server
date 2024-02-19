#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Garvin
Email: garvin210905@gmail.com
Created Time: 2024/2/19 11:46
Description: This script is used to do something.
"""

import os
import sys

SRC_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))
sys.path.append(SRC_PATH)

from util.logger_util import LoggerUtil

logger = LoggerUtil(log_name="common")


def main():
    logger.info("main")


if __name__ == "__main__":
    main()
