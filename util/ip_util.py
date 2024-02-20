#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Garvin
Email: garvin210905@gmail.com
Created Time: 2024/2/19 23:42
Description: This script is used to do something.
"""

import os
import socket
import struct
import io
from typing import Union

BASE_PATH = os.path.dirname(os.path.dirname(__file__))
RESOURCE_PATH = os.path.join(BASE_PATH, "resource")
DATA_PATH = os.path.join(RESOURCE_PATH, "data")
IP_DB_PATH = os.path.join(DATA_PATH, "ip_region_map.xdb")


class IpUtil(object):
    def __init__(self):
        self.content_buff = None

    def get_region_by_ip(self, ip: str) -> tuple[str, str]:
        if not self.valid_ip(ip):
            err = f"Invalid ip: {ip}"
            return err, ""
        self._refresh_cb()
        return "", self._search_by_ip_long(self._ip_to_long(ip))

    def _search_by_ip_long(self, ip: int) -> str:
        # xdb默认参数
        header_info_length = 256
        vector_index_cols = 256
        vector_index_size = 8
        segment_index_size = 14

        # locate the segment index block based on the vector index
        il0 = int((ip >> 24) & 0xFF)
        il1 = int((ip >> 16) & 0xFF)
        idx = il0 * vector_index_cols * vector_index_size + il1 * vector_index_size

        s_ptr = self._get_long(self.content_buff, header_info_length + idx)
        e_ptr = self._get_long(self.content_buff, header_info_length + idx + 4)

        # binary search the segment index block to get the region info
        data_len = data_ptr = int(-1)
        l = int(0)
        h = int((e_ptr - s_ptr) / segment_index_size)
        while l <= h:
            m = int((l + h) >> 1)
            p = int(s_ptr + m * segment_index_size)
            # read the segment index
            buffer_sip = self.read_buffer(p, segment_index_size)
            sip = self._get_long(buffer_sip, 0)
            if ip < sip:
                h = m - 1
            else:
                eip = self._get_long(buffer_sip, 4)
                if ip > eip:
                    l = m + 1
                else:
                    data_len = self._get_int2(buffer_sip, 8)
                    data_ptr = self._get_long(buffer_sip, 10)
                    break

        # empty match interception
        if data_ptr < 0:
            return ""

        buffer_string = self.read_buffer(data_ptr, data_len)
        return_string = buffer_string.decode("utf-8")
        return return_string

    def read_buffer(self, offset: int, length: int) -> Union[str, bytes]:
        return self.content_buff[offset:offset + length]

    @staticmethod
    def _get_long(b: Union[str, bytes], offset: int) -> int:
        if len(b[offset:offset + 4]) == 4:
            return struct.unpack('I', b[offset:offset + 4])[0]
        return 0

    @staticmethod
    def _get_int2(b: Union[str, bytes], offset: int) -> int:
        return (b[offset] & 0x000000FF) | (b[offset + 1] & 0x0000FF00)

    @staticmethod
    def _ip_to_long(ip: str) -> int:
        _ip = socket.inet_aton(ip)
        return struct.unpack("!L", _ip)[0]

    @staticmethod
    def valid_ip(ip: str) -> bool:
        p = ip.split(".")
        if len(p) != 4:
            return False
        for pp in p:
            if not pp.isdigit():
                return False
            if len(pp) > 3:
                return False
            if int(pp) > 255:
                return False
        return True

    def _refresh_cb(self) -> None:
        if self.content_buff is None:
            f = io.open(IP_DB_PATH, "rb")
            self.content_buff = f.read()
            f.close()

    @staticmethod
    def get_ip_address() -> str:
        # 获取主私网IP 不是公网IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            # 使用连接到公共IP地址的域名，然后获取本地IP地址
            s.connect(('8.8.8.8', 80))
            ip_address = s.getsockname()[0]
        finally:
            s.close()
        return ip_address


class_ip_util = IpUtil()
