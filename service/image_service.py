#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Garvin
Email: garvin210905@gmail.com
Created Time: 2024/2/20 14:22
Description: This script is used to do something.
"""
import base64
import os
import sys

BASE_PATH = os.path.dirname(os.path.dirname(__file__))
RESOURCE_PATH = os.path.join(BASE_PATH, "resource")
IMAGE_PATH = os.path.join(RESOURCE_PATH, "image")
sys.path.append(BASE_PATH)

from util.logger_util import logger_info, logger_error
from util.common_util import CommonUtil


class ImageService:
    def __init__(self):
        pass

    @staticmethod
    def upload_image(file_name: str, file_content: bytes) -> str:
        suffix = file_name.split('.')[1]
        n = CommonUtil.str_to_md5(str(file_content))
        md5_file_name = f"{n}.{suffix}"
        file_path = os.path.join(IMAGE_PATH, md5_file_name)
        if CommonUtil.file_exist(file_path):
            return md5_file_name
        with open(file_path, 'wb') as save_file:
            save_file.write(file_content)
        return md5_file_name

    @staticmethod
    def valid_image(file_name: str) -> bool:
        l = file_name.split('.')
        if len(l) != 2:
            return False
        if l[1] not in ['jpg', 'gif', 'png']:
            return False
        return True

    @staticmethod
    def get_image(image_name: str) -> tuple[str, bytes]:
        file_path = os.path.join(IMAGE_PATH, image_name)
        if not CommonUtil.file_exist(file_path):
            err = f"Image not exists - {image_name}"
            logger_info.info(err)
            return err, b""
        with open(file_path, 'rb') as file:
            file_content = file.read()
        return "", file_content
