#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Garvin
Email: garvin210905@gmail.com
Created Time: 2024/2/19 14:52
Description: This script is used to do something.
"""

import logging
import os
import re
from logging.handlers import TimedRotatingFileHandler
from typing import Literal

BASE_PATH = os.path.dirname(os.path.dirname(__file__))
LOG_PATH = os.path.join(BASE_PATH, "log")

LOG_FORMATTER = logging.Formatter(
    "%(asctime)s|%(levelname)s|%(filename)s:%(lineno)d|%(message)s",
    "%Y-%m-%d %H:%M:%S",
)
LOGGER_LEVEL = {
    "debug": logging.DEBUG,
    "info": logging.INFO,
    "warning": logging.WARNING,
    "error": logging.ERROR,
    "critical": logging.CRITICAL,
}


def logger_split(
        log_name: str = "split.log",
        log_dir: str = LOG_PATH,
        log_level: Literal["debug", "info", "warning", "error", "critical"] = "info",
        log_keep_days: int = 15,
) -> logging.Logger:
    log_path = os.path.join(log_dir, log_name)
    logger = logging.getLogger(log_path)

    logger.setLevel(LOGGER_LEVEL.get(log_level, "info"))

    log_screen = logging.StreamHandler()
    log_screen.setFormatter(LOG_FORMATTER)
    logger.addHandler(log_screen)

    try:
        file_handler = TimedRotatingFileHandler(
            filename=log_path,
            when="MIDNIGHT",
            interval=1,
            backupCount=log_keep_days,
        )
        file_handler.suffix = "%Y-%m-%d.log"
        file_handler.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}.log$")
        file_handler.setFormatter(LOG_FORMATTER)
        logger.addHandler(file_handler)
    except FileNotFoundError as e:
        logger.error(e)
    return logger


def logger_common(
        log_name: str = "common.log",
        log_dir: str = LOG_PATH,
        log_level: Literal["debug", "info", "warning", "error", "critical"] = "info",
) -> logging.Logger:
    log_path = os.path.join(log_dir, log_name)
    logger = logging.getLogger(log_path)

    logger.setLevel(LOGGER_LEVEL.get(log_level, "info"))

    log_screen = logging.StreamHandler()
    log_screen.setFormatter(LOG_FORMATTER)
    logger.addHandler(log_screen)
    try:
        file_handler = TimedRotatingFileHandler(filename=log_path)
        file_handler.setFormatter(LOG_FORMATTER)
        logger.addHandler(file_handler)
    except FileNotFoundError as e:
        logger.error(e)
    return logger
