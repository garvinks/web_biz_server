#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Garvin
Email: garvin210905@gmail.com
Created Time: 2024/2/20 11:33
Description: This script is used to do something.
"""
import json
import mimetypes
import os
import sys

import tornado

BASE_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_PATH)

from util.response_util import ResponseUtil
from util.filter_util import class_filter_util
from service.image_service import ImageService


class ImageController(tornado.web.RequestHandler):
    def get(self):
        self.write(ResponseUtil.success())


class ImageControllerGetImage(tornado.web.RequestHandler):
    def get(self):
        req = json.loads(self.request.body.decode('utf-8'))
        image_name = req.get('image_name', None)
        if not image_name:
            self.write(ResponseUtil.error(data='Missing Param: image_name'))
            return
        err, rsp = ImageService.get_image(image_name)
        if err:
            self.write(ResponseUtil.error(data=err))
            return
        # 限流
        if not class_filter_util.filter_by_str(self.request.remote_ip + 'get_image'):
            self.write(ResponseUtil.error(data='please wait one minute later'))
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
        # 限流
        if not class_filter_util.filter_by_str(self.request.remote_ip + 'upload_image'):
            self.write(ResponseUtil.error(data='please wait one minute later'))
            return
        file_content = file_dict['body']
        n = ImageService.upload_image(file_name, file_content)
        image_url = f'http://120.24.6.195:9999/image/get_image?image_name={n}'
        self.write(ResponseUtil.success(data=image_url))
