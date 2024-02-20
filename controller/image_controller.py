#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Garvin
Email: garvin210905@gmail.com
Created Time: 2024/2/20 11:33
Description: This script is used to do something.
"""
import mimetypes
import os
import sys

import tornado

BASE_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_PATH)

from util.response_util import ResponseUtil
from service.image_service import ImageService


class ImageController(tornado.web.RequestHandler):
    def get(self):
        self.write(ResponseUtil.success())


class ImageControllerGetImage(tornado.web.RequestHandler):
    def get(self):
        image_name = self.get_argument('image_name', None)
        if not image_name:
            self.write(ResponseUtil.error(data='Missing Param: image_name'))
            return
        err, rsp = ImageService.get_image(image_name)
        if err:
            self.write(ResponseUtil.error(data=err))
            return
        # 使用mimetypes模块动态获取Content-Type
        content_type, _ = mimetypes.guess_type(image_name)
        if content_type:
            self.set_header('Content-Type', content_type)
        self.write(rsp)


class ImageControllerUploadImage(tornado.web.RequestHandler):
    def post(self):
        file_dict_list = self.request.files.get('image_file', None)
        if not file_dict_list:
            self.write(ResponseUtil.error(data='Missing Param: image_file'))
            return
        file_dict = file_dict_list[0]
        file_name = file_dict['filename']
        if not ImageService.valid_image(file_name):
            self.write(ResponseUtil.error(data=f'file_name Not Valid: {file_name}'))
            return
        file_content = file_dict['body']
        n = ImageService.upload_image(file_name, file_content)
        image_url = f'http://120.24.6.195:9999/image/get_image?image_name={n}'
        self.write(ResponseUtil.success(data=image_url))