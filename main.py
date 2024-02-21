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
from controller.health_controller import HealthController
from controller.image_controller import ImageController, ImageControllerGetImage, ImageControllerUploadImage


def make_app():
    return tornado.web.Application([
        (r"/health", HealthController),

        (r"/image", ImageController),
        (r"/image/get_image", ImageControllerGetImage),
        (r"/image/upload_image", ImageControllerUploadImage),

    ])


def init() -> None:
    SqliteStructInit.execute_init()
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
