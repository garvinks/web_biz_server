#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Garvin
Email: garvin210905@gmail.com
Created Time: 2024/2/22 9:43
Description: This script is used to do something.
"""
from typing import NamedTuple


class LotteryEntity(NamedTuple):
    id: int


class LotteryEntityDoubleColorBallOrder(NamedTuple):
    """
    t_lottery_order
    t_lottery_prize
    """
    id: int
    trace_id: str  # 32位 uuid4
    prize_id: int
    order_code: str
    status: int  # 2已兑换 0未兑换 1已中奖 3已过期（金额加入奖池）
    prize_level: int  # 奖项等级 0未中奖 1~6等奖（兑奖需要记录用户IP）
    created_at: int
    updated_at: int


class LotteryEntityDoubleColorBallPrize(NamedTuple):
    id: int
    order_no: str  # DCB2024020101
    order_date: str  # 2024-02-22
    prize_code: str  # 中奖号码
    prize_pool: int  # 上一期剩下的奖金（减去所有的中将之后剩下的金额）
    created_at: int
    expired_at: int


class LotteryEntityDoubleColorBallClaim(NamedTuple):
    id: int
    order_id: int
    ip_address: str
    country: str
    province: str
    city: str
    net: str
    created_at: int
