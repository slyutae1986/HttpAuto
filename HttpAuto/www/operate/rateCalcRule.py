#! /usr/bin/env python
# -*- coding:utf-8 -*-

import decimal

'''
第一步：设置math环境

第一步：计算服务费和利息

第二步：判断服务费和利息是否是小数，如果是，四舍六入五成双后返回两位小数，如果不是，直接返回整数

'''


class rateCalcRule(object):

    def __init__(self, amount, interestrate, expenses, period, borrowdays):
        self.amount = decimal.Decimal(amount)
        self.period = decimal.Decimal(period)
        self.expenses = decimal.Decimal(expenses)
        self.borrowdays = decimal.Decimal(borrowdays)
        self.interestrate = decimal.Decimal(interestrate)

    def calcRuleOne(self):
        interestFee = self.interestrate / self.period * self.borrowdays * self.amount
        if isinstance(interestFee, int) is True:
            self.interest = interestFee
            return self.interest
        else:
            self.interest = round(decimal.Decimal(str(interestFee)))
            return int(self.interest)

    def calcRuleTwo(self):
        serviceFee = (self.expenses - self.interestrate / self.period * self.borrowdays) * self.amount
        if isinstance(serviceFee, int) is True:
            self.serviceFee = serviceFee
            return self.serviceFee
        else:
            self.service = round(decimal.Decimal(str(serviceFee)))
            return int(self.service)