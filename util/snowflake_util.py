#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Garvin
Email: garvin210905@gmail.com
Created Time: 2024/2/22 15:10
Description: This script is used to do something.
"""
import time
import threading


class SnowflakeUtil:
    def __init__(self, datacenter_id: int = 1, worker_id: int = 1):
        self.epoch = 1609459200000  # 自定义起始时间，例如 2021-01-01 00:00:00
        self.datacenter_id = datacenter_id
        self.worker_id = worker_id
        self.sequence = 0
        self.last_timestamp = -1
        self.lock = threading.Lock()

    @staticmethod
    def _get_timestamp():
        return int(time.time() * 1000)

    def _wait_for_next_millisecond(self, last_timestamp):
        timestamp = self._get_timestamp()
        while timestamp <= last_timestamp:
            timestamp = self._get_timestamp()
        return timestamp

    def get_id(self):
        with self.lock:
            timestamp = self._get_timestamp()

            if timestamp < self.last_timestamp:
                raise Exception("Clock moved backwards. Refusing to generate id for %d milliseconds" % (
                        self.last_timestamp - timestamp))

            if timestamp == self.last_timestamp:
                self.sequence = (self.sequence + 1) & 0xFFF
                if self.sequence == 0:
                    timestamp = self._wait_for_next_millisecond(self.last_timestamp)
            else:
                self.sequence = 0

            self.last_timestamp = timestamp

            return ((timestamp - self.epoch) << 22) | (self.datacenter_id << 17) | (
                    self.worker_id << 12) | self.sequence


class_snowflake_util = SnowflakeUtil()
