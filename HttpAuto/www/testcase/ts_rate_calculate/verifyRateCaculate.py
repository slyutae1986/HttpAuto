#! user/bin/env python
# -*-coding:utf-8 -*-

import unittest
import datetime
from www.common.other import others
from www.common.excel import rData
from www.api.rateSysApi import *
from www.operate.rateCalcRule import rateCalcRule
from www.operate.datacalc import datecalculate

"""
Package the rate calculate api,write the test suite here

Author by slyutae on 2017.09.07

Api:

"""




class rateCalc(unittest.TestCase):

    config = rData('dsq_kaola_14')


    def test_RateCalc_500(self):
        calconfig = rateSystem()
        nowdate = datetime.date.today()
        obj = rateCalcRule(50000, self.config.interestrate, self.config.expenses, self.config.countdays, self.config.borrowdays )
        interestFee = obj.calcRuleOne()
        serviceFee = obj.calcRuleTwo()
        rsp = calconfig.calculate_dsq(self.config.type,'DSQ',str(nowdate),1,50000,self.config.product_number)
        if rsp.code == '0':
            print 'Error'
        else:
            self.assertEqual(rsp.caculate_result['grant']['amout'],50000)
            self.assertEqual(rsp.caculate_result['grant']['period'],self.config.period)
            self.assertEqual(rsp.caculate_result['grant']['date'],self.config.date)
            self.assertEqual(rsp.caculate_result['principal'][0]['amount'],50000)
            self.assertEqual(rsp.caculate_result['principal'][0]['date'],)
            self.assertEqual(rsp.caculate_result['principal'][0]['period'],1)
            self.assertEqual(rsp.caculate_result['interest'][0]['repay_type'],'ending_deduction')
            self.assertEqual(rsp.caculate_result['interest'][0]['date'])
            self.assertEqual(rsp.caculate_result['interest'][0]['amount'],interestFee)
            self.assertEqual(rsp.caculate_result['fee']['service'][0]['repay_type'],'ending_deduction')
            self.assertEqual(rsp.caculate_result['fee']['service'][0]['period'],1)
            self.assertEqual(rsp.caculate_result['fee']['service'][0]['date'], )
            self.assertEqual(rsp.caculate_result['fee']['service'][0]['amount'],serviceFee)
            self.assertEqual(rsp.cauclate_result['fee']['audit'][0]['repay_type'],'ending_deduction')
            self.assertEqual(rsp.cauclate_result['fee']['audit'][0]['period'], 1)
            self.assertEqual(rsp.cauclate_result['fee']['audit'][0]['date'],)
            self.assertEqual(rsp.cauclate_result['fee']['audit'][0]['amount'],self.config.auditfee)

    def test_RateCalc_600(self):
        calconfig = rateSystem()
        nowdate = others().datenow
        rsp = calconfig.calculate_dsq(self.config.type,'DSQ',str(nowdate),1,60000,self.config.product_number)
        if rsp.code == '0':
            print 'Error'
        else:
            self.assertEqual(rsp.caculate_result['amout'],self.config.grant_amount)
            self.assertEqual(rsp.caculate_result['period'],self.config.period)
            self.assertEqual(rsp.caculate_result['date'],self.config.date)

def suite ():
    suite = unittest.TestSuite()
    suite.addTest(rateCalc("test_RateCalc_500"))
    #suite.addTest(rateCalc("test_RateCalc_600"))
    return suite