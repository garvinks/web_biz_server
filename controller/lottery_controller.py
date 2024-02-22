#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Garvin
Email: garvin210905@gmail.com
Created Time: 2024/2/22 10:04
Description: This script is used to do something.
"""
import json
import os
import sys

import tornado

BASE_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_PATH)

from util.response_util import ResponseUtil


class LotteryController(tornado.web.RequestHandler):
    def get(self):
        self.write(ResponseUtil.success())


class LotteryControllerDoubleColorBall(tornado.web.RequestHandler):
    def get(self):
        self.write(ResponseUtil.success())


class LotteryControllerDoubleColorBallBuyTicket(tornado.web.RequestHandler):
    def post(self):
        req = json.loads(self.request.body.decode('utf-8'))
        red_balls = req.get('red_balls', [])
        blue_ball = req.get('blue_ball', 0)
        if len(red_balls) != 6:
            self.write(ResponseUtil.error_param(req))
            return
        for i in red_balls:
            if type(i) is not int or i < 1 or i > 33:
                self.write(ResponseUtil.error_param(req))
                return
        if type(blue_ball) is not int or blue_ball < 1 or blue_ball > 16:
            self.write(ResponseUtil.error_param(req))
            return

        # if not file_dict_list:
        #     self.write(ResponseUtil.error(data='Missing Param: image_file'))
        #     return
        self.write(ResponseUtil.success())


class LotteryControllerDoubleColorBallClaimPrize(tornado.web.RequestHandler):
    def get(self):
        self.write(ResponseUtil.success())
