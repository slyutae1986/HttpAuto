#! /usr/bin/env python
# -*- coding:utf-8 -*-

"""
Package the rate calculate api

Author by slyutae on 2017.09.05

"""

from www.common.httpbase import *
from www.common.other import others



class rateSystem:

    def __init__(self):
        self.packHttpBase = httpbase()

    def calculate_dsq(self,type = None,key = None,from_system = None,sign_date = None,period_count = None,
                      applay_amout = None,product_number = None):
        url ='v5/rate/calculate'
        data = {}
        data['sign_date'] = sign_date
        data['period_count'] = period_count
        data['apply_amount'] = applay_amout
        data['product_number'] = product_number
        orgdata = {}
        orgdata['type'] = type
        orgdata['key'] = others().randomString
        orgdata['from_system'] = from_system
        orgdata['data'] = data
        self.packHttpBase.sendPost(orgdata,url)
        return self.packHttpBase.body

    def calculate_kfq(self):
        pass



