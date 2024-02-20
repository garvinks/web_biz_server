#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Garvin
Email: garvin210905@gmail.com
Created Time: 2024/2/20 11:00
Description: This script is used to do something.
"""

import os
import sys
import json

BASE_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_PATH)

from dto.response_dto import ResponseDTO


class ResponseUtil(object):
    @staticmethod
    def success(code: int = 0, message: str = "", data: object = None):
        return json.dumps(ResponseDTO(success=True, code=code, message=message, data=data)._asdict())

    @staticmethod
    def error(code: int = 0, message: str = "", data: object = None):
        return json.dumps(ResponseDTO(success=False, code=code, message=message, data=data)._asdict())
