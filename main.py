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

from util.logger_util import logger_split
from util.ip_util import class_ip_util
from controller.health_controller import HealthController

logger_info = logger_split(log_name="web_biz_server.log", log_screen=False)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        ip = self.request.remote_ip
        self.write(f"Hello, world. ip:{ip} region:{class_ip_util.get_region_by_ip(ip)}")


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/health", HealthController),
    ])


async def main():
    logger_info.info("Starting web_biz_server...")
    app = make_app()
    app.listen(9999)
    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())
