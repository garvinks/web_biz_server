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

BASE_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_PATH)

from util.logger_util import logger_info, logger_error


class UserService(object):
    def __init__(self):
        pass

    def create_user(self):
        pass

