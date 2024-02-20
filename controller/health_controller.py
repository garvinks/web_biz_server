#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Garvin
Email: garvin210905@gmail.com
Created Time: 2024/2/20 10:49
Description: This script is used to do something.
"""
import os
import sys

import tornado

BASE_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_PATH)

from util.response_util import ResponseUtil


class HealthController(tornado.web.RequestHandler):
    def get(self):
        self.write(ResponseUtil.success())
