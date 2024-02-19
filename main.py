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
from util.logger_util import logger_common

logger_info = logger_split(log_name="web_biz_server.log")
logger_error = logger_common(log_name="error.log")


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        ip = self.request.remote_ip
        logger_info.info(ip)
        logger_info.info(type(ip))
        logger_error.info("main")
        self.write("Hello, world" + ip)


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])


async def main():
    app = make_app()
    app.listen(9999)
    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())
