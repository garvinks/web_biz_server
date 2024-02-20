#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Garvin
Email: garvin210905@gmail.com
Created Time: 2024/2/20 11:00
Description: This script is used to do something.
"""
from typing import NamedTuple


class ResponseDTO(NamedTuple):
    success: bool
    code: int
    message: str
    data: object
