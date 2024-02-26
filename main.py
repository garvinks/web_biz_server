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

import asyncio
import tornado

BASE_PATH = os.path.dirname(__file__)
sys.path.append(BASE_PATH)

from util.logger_util import logger_info
from init.sqlite_struct_init import SqliteStructInit
from init.lottery_prize_init import LotteryPrizeInit
from controller.health_controller import HealthController
from controller.user_controller import UserController
from controller.image_controller import ImageController, ImageControllerGetImage, ImageControllerUploadImage
from controller.lottery_controller import LotteryController, LotteryControllerDoubleColorBall, \
    LotteryControllerDoubleColorBallBuyTicket, LotteryControllerDoubleColorBallClaimPrize


def make_app():
    return tornado.web.Application([
        # 健康检查
        (r"/health", HealthController),

        # 用户模块
        (r"/user", UserController),

        # 图床功能
        (r"/image", ImageController),
        (r"/image/get_image", ImageControllerGetImage),
        (r"/image/upload_image", ImageControllerUploadImage),

        # 彩票模块
        (r"/lottery", LotteryController),
        (r"/lottery/double_color_ball", LotteryControllerDoubleColorBall),
        (r"/lottery/double_color_ball/buy_ticket", LotteryControllerDoubleColorBallBuyTicket),
        (r"/lottery/double_color_ball/claim_prize", LotteryControllerDoubleColorBallClaimPrize),

    ])


def init() -> None:
    if not SqliteStructInit.execute_init():
        raise Exception('SqliteStructInit.execute_init Error')
    if not LotteryPrizeInit.set_zero_prize():
        raise Exception('LotteryPrizeInit.set_zero_prize Error')
    return


async def main():
    logger_info.info("Starting web_biz_server")
    init()
    logger_info.info("init server")
    app = make_app()
    app.listen(9999)
    logger_info.info("run server")
    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())
