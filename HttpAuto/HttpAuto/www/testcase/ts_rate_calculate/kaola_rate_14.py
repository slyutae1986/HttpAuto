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




class kaola_rate_14(unittest.TestCase):

    #获取excel数据
    config = rData('dsq_kaola_14')
    #获取delta时间
    date = datecalculate(14).datecalc()


    def test_kaola_rate_14_500(self):
        #创建接口模型对象
        calconfig = rateSystem()
        #计算服务费和利息
        obj = rateCalcRule(50000, kaola_rate_14.config.interestrate, kaola_rate_14.config.expenses, kaola_rate_14.config.countdays, kaola_rate_14.config.borrowdays )
        #准备响应体参数
        rsp = calconfig.calculate_dsq(kaola_rate_14.config.type,str(int(others().randomString())),kaola_rate_14.config.from_system,str(datetime.date.today()),'50000',1,kaola_rate_14.config.product_number)
        if rsp.code == 0:
            print 'rsp.code != 0,Error'
        else:
            self.assertEqual(rsp.data['calculate_result']['grant']['amount'],50000)
            self.assertEqual(rsp.data['calculate_result']['grant']['period'],0)
            self.assertEqual(rsp.data['calculate_result']['grant']['date'],str(datetime.date.today()))
            self.assertEqual(rsp.data['calculate_result']['principal'][0]['amount'],50000)
            self.assertEqual(rsp.data['calculate_result']['principal'][0]['date'],kaola_rate_14.date)
            self.assertEqual(rsp.data['calculate_result']['principal'][0]['period'],1)
            self.assertEqual(rsp.data['calculate_result']['interest'][0]['date'],kaola_rate_14.date)
            self.assertEqual(rsp.data['calculate_result']['interest'][0]['amount'],obj.calcRuleOne())
            self.assertEqual(rsp.data['calculate_result']['fee']['service'][0]['repay_type'],'ending_deduction')
            self.assertEqual(rsp.data['calculate_result']['fee']['service'][0]['period'],1)
            self.assertEqual(rsp.data['calculate_result']['fee']['service'][0]['date'], kaola_rate_14.date)
            self.assertEqual(rsp.data['calculate_result']['fee']['service'][0]['amount'],obj.calcRuleTwo())
            self.assertEqual(rsp.data['calculate_result']['fee']['audit'][0]['repay_type'],'ending_deduction')
            self.assertEqual(rsp.data['calculate_result']['fee']['audit'][0]['period'], 1)
            self.assertEqual(rsp.data['calculate_result']['fee']['audit'][0]['date'],kaola_rate_14.date)
            self.assertEqual(rsp.data['calculate_result']['fee']['audit'][0]['amount'],int(self.config.auditfee))

    def test_kaola_rate_14_600(self):
        #创建接口模型对象
        calconfig = rateSystem()
        #计算服务费和利息
        obj = rateCalcRule(60000, kaola_rate_14.config.interestrate, kaola_rate_14.config.expenses, kaola_rate_14.config.countdays, kaola_rate_14.config.borrowdays )
        #准备响应体参数
        rsp = calconfig.calculate_dsq(kaola_rate_14.config.type,str(int(others().randomString())),kaola_rate_14.config.from_system,str(datetime.date.today()),'60000',1,kaola_rate_14.config.product_number)
        if rsp.code == 0:
            print 'rsp.code != 0,Error'
        else:
            self.assertEqual(rsp.data['calculate_result']['grant']['amount'],60000)
            self.assertEqual(rsp.data['calculate_result']['grant']['period'],0)
            self.assertEqual(rsp.data['calculate_result']['grant']['date'],str(datetime.date.today()))
            self.assertEqual(rsp.data['calculate_result']['principal'][0]['amount'],60000)
            self.assertEqual(rsp.data['calculate_result']['principal'][0]['date'],kaola_rate_14.date)
            self.assertEqual(rsp.data['calculate_result']['principal'][0]['period'],1)
            self.assertEqual(rsp.data['calculate_result']['interest'][0]['date'],kaola_rate_14.date)
            self.assertEqual(rsp.data['calculate_result']['interest'][0]['amount'],obj.calcRuleOne())
            self.assertEqual(rsp.data['calculate_result']['fee']['service'][0]['repay_type'],'ending_deduction')
            self.assertEqual(rsp.data['calculate_result']['fee']['service'][0]['period'],1)
            self.assertEqual(rsp.data['calculate_result']['fee']['service'][0]['date'], kaola_rate_14.date)
            self.assertEqual(rsp.data['calculate_result']['fee']['service'][0]['amount'],obj.calcRuleTwo())
            self.assertEqual(rsp.data['calculate_result']['fee']['audit'][0]['repay_type'],'ending_deduction')
            self.assertEqual(rsp.data['calculate_result']['fee']['audit'][0]['period'], 1)
            self.assertEqual(rsp.data['calculate_result']['fee']['audit'][0]['date'],kaola_rate_14.date)
            self.assertEqual(rsp.data['calculate_result']['fee']['audit'][0]['amount'],int(self.config.auditfee))

    def test_kaola_rate_14_700(self):
        # 创建接口模型对象
        calconfig = rateSystem()
        # 计算服务费和利息
        obj = rateCalcRule(70000, kaola_rate_14.config.interestrate, kaola_rate_14.config.expenses, kaola_rate_14.config.countdays,kaola_rate_14.config.borrowdays)
        # 准备响应体参数
        rsp = calconfig.calculate_dsq(kaola_rate_14.config.type, str(int(others().randomString())),kaola_rate_14.config.from_system, str(datetime.date.today()), '70000', 1,kaola_rate_14.config.product_number)
        if rsp.code == 0:
            print 'rsp.code != 0,Error'
        else:
            self.assertEqual(rsp.data['calculate_result']['grant']['amount'], 70000)
            self.assertEqual(rsp.data['calculate_result']['grant']['period'], 0)
            self.assertEqual(rsp.data['calculate_result']['grant']['date'], str(datetime.date.today()))
            self.assertEqual(rsp.data['calculate_result']['principal'][0]['amount'], 70000)
            self.assertEqual(rsp.data['calculate_result']['principal'][0]['date'], kaola_rate_14.date)
            self.assertEqual(rsp.data['calculate_result']['principal'][0]['period'], 1)
            self.assertEqual(rsp.data['calculate_result']['interest'][0]['date'], kaola_rate_14.date)
            self.assertEqual(rsp.data['calculate_result']['interest'][0]['amount'], obj.calcRuleOne())
            self.assertEqual(rsp.data['calculate_result']['fee']['service'][0]['repay_type'], 'ending_deduction')
            self.assertEqual(rsp.data['calculate_result']['fee']['service'][0]['period'], 1)
            self.assertEqual(rsp.data['calculate_result']['fee']['service'][0]['date'], kaola_rate_14.date)
            self.assertEqual(rsp.data['calculate_result']['fee']['service'][0]['amount'], obj.calcRuleTwo())
            self.assertEqual(rsp.data['calculate_result']['fee']['audit'][0]['repay_type'], 'ending_deduction')
            self.assertEqual(rsp.data['calculate_result']['fee']['audit'][0]['period'], 1)
            self.assertEqual(rsp.data['calculate_result']['fee']['audit'][0]['date'], kaola_rate_14.date)
            self.assertEqual(rsp.data['calculate_result']['fee']['audit'][0]['amount'], int(self.config.auditfee))

    def test_kaola_rate_14_800(self):
        # 创建接口模型对象
        calconfig = rateSystem()
        # 计算服务费和利息
        obj = rateCalcRule(80000, kaola_rate_14.config.interestrate, kaola_rate_14.config.expenses, kaola_rate_14.config.countdays,kaola_rate_14.config.borrowdays)
        # 准备响应体参数
        rsp = calconfig.calculate_dsq(kaola_rate_14.config.type, str(int(others().randomString())),kaola_rate_14.config.from_system, str(datetime.date.today()), '80000', 1,kaola_rate_14.config.product_number)
        if rsp.code == 0:
            print 'rsp.code != 0,Error'
        else:
            self.assertEqual(rsp.data['calculate_result']['grant']['amount'], 80000)
            self.assertEqual(rsp.data['calculate_result']['grant']['period'], 0)
            self.assertEqual(rsp.data['calculate_result']['grant']['date'], str(datetime.date.today()))
            self.assertEqual(rsp.data['calculate_result']['principal'][0]['amount'], 80000)
            self.assertEqual(rsp.data['calculate_result']['principal'][0]['date'], kaola_rate_14.date)
            self.assertEqual(rsp.data['calculate_result']['principal'][0]['period'], 1)
            self.assertEqual(rsp.data['calculate_result']['interest'][0]['date'], kaola_rate_14.date)
            self.assertEqual(rsp.data['calculate_result']['interest'][0]['amount'], obj.calcRuleOne())
            self.assertEqual(rsp.data['calculate_result']['fee']['service'][0]['repay_type'], 'ending_deduction')
            self.assertEqual(rsp.data['calculate_result']['fee']['service'][0]['period'], 1)
            self.assertEqual(rsp.data['calculate_result']['fee']['service'][0]['date'], kaola_rate_14.date)
            self.assertEqual(rsp.data['calculate_result']['fee']['service'][0]['amount'], obj.calcRuleTwo())
            self.assertEqual(rsp.data['calculate_result']['fee']['audit'][0]['repay_type'], 'ending_deduction')
            self.assertEqual(rsp.data['calculate_result']['fee']['audit'][0]['period'], 1)
            self.assertEqual(rsp.data['calculate_result']['fee']['audit'][0]['date'], kaola_rate_14.date)
            self.assertEqual(rsp.data['calculate_result']['fee']['audit'][0]['amount'], int(self.config.auditfee))

    def test_kaola_rate_14_900(self):
        # 创建接口模型对象
        calconfig = rateSystem()
        # 计算服务费和利息
        obj = rateCalcRule(90000, kaola_rate_14.config.interestrate, kaola_rate_14.config.expenses, kaola_rate_14.config.countdays,kaola_rate_14.config.borrowdays)
        # 准备响应体参数
        rsp = calconfig.calculate_dsq(kaola_rate_14.config.type, str(int(others().randomString())),kaola_rate_14.config.from_system, str(datetime.date.today()), '90000', 1,kaola_rate_14.config.product_number)
        if rsp.code == 0:
            print 'rsp.code != 0,Error'
        else:
            self.assertEqual(rsp.data['calculate_result']['grant']['amount'], 90000)
            self.assertEqual(rsp.data['calculate_result']['grant']['period'], 0)
            self.assertEqual(rsp.data['calculate_result']['grant']['date'], str(datetime.date.today()))
            self.assertEqual(rsp.data['calculate_result']['principal'][0]['amount'], 90000)
            self.assertEqual(rsp.data['calculate_result']['principal'][0]['date'], kaola_rate_14.date)
            self.assertEqual(rsp.data['calculate_result']['principal'][0]['period'], 1)
            self.assertEqual(rsp.data['calculate_result']['interest'][0]['date'], kaola_rate_14.date)
            self.assertEqual(rsp.data['calculate_result']['interest'][0]['amount'], obj.calcRuleOne())
            self.assertEqual(rsp.data['calculate_result']['fee']['service'][0]['repay_type'], 'ending_deduction')
            self.assertEqual(rsp.data['calculate_result']['fee']['service'][0]['period'], 1)
            self.assertEqual(rsp.data['calculate_result']['fee']['service'][0]['date'], kaola_rate_14.date)
            self.assertEqual(rsp.data['calculate_result']['fee']['service'][0]['amount'], obj.calcRuleTwo())
            self.assertEqual(rsp.data['calculate_result']['fee']['audit'][0]['repay_type'], 'ending_deduction')
            self.assertEqual(rsp.data['calculate_result']['fee']['audit'][0]['period'], 1)
            self.assertEqual(rsp.data['calculate_result']['fee']['audit'][0]['date'], kaola_rate_14.date)
            self.assertEqual(rsp.data['calculate_result']['fee']['audit'][0]['amount'], int(self.config.auditfee))

    def test_kaola_rate_14_1000(self):
        # 创建接口模型对象
        calconfig = rateSystem()
        # 计算服务费和利息
        obj = rateCalcRule(100000, kaola_rate_14.config.interestrate, kaola_rate_14.config.expenses, kaola_rate_14.config.countdays,kaola_rate_14.config.borrowdays)
        # 准备响应体参数
        rsp = calconfig.calculate_dsq(kaola_rate_14.config.type, str(int(others().randomString())),kaola_rate_14.config.from_system, str(datetime.date.today()), '100000', 1,kaola_rate_14.config.product_number)
        if rsp.code == 0:
            print 'rsp.code != 0,Error'
        else:
            self.assertEqual(rsp.data['calculate_result']['grant']['amount'], 100000)
            self.assertEqual(rsp.data['calculate_result']['grant']['period'], 0)
            self.assertEqual(rsp.data['calculate_result']['grant']['date'], str(datetime.date.today()))
            self.assertEqual(rsp.data['calculate_result']['principal'][0]['amount'], 100000)
            self.assertEqual(rsp.data['calculate_result']['principal'][0]['date'], kaola_rate_14.date)
            self.assertEqual(rsp.data['calculate_result']['principal'][0]['period'], 1)
            self.assertEqual(rsp.data['calculate_result']['interest'][0]['date'], kaola_rate_14.date)
            self.assertEqual(rsp.data['calculate_result']['interest'][0]['amount'], obj.calcRuleOne())
            self.assertEqual(rsp.data['calculate_result']['fee']['service'][0]['repay_type'], 'ending_deduction')
            self.assertEqual(rsp.data['calculate_result']['fee']['service'][0]['period'], 1)
            self.assertEqual(rsp.data['calculate_result']['fee']['service'][0]['date'], kaola_rate_14.date)
            self.assertEqual(rsp.data['calculate_result']['fee']['service'][0]['amount'], obj.calcRuleTwo())
            self.assertEqual(rsp.data['calculate_result']['fee']['audit'][0]['repay_type'], 'ending_deduction')
            self.assertEqual(rsp.data['calculate_result']['fee']['audit'][0]['period'], 1)
            self.assertEqual(rsp.data['calculate_result']['fee']['audit'][0]['date'], kaola_rate_14.date)
            self.assertEqual(rsp.data['calculate_result']['fee']['audit'][0]['amount'], int(self.config.auditfee))

    def test_kaola_rate_14_1100(self):
        # 创建接口模型对象
        calconfig = rateSystem()
        # 计算服务费和利息
        obj = rateCalcRule(110000, kaola_rate_14.config.interestrate, kaola_rate_14.config.expenses, kaola_rate_14.config.countdays,kaola_rate_14.config.borrowdays)
        # 准备响应体参数
        rsp = calconfig.calculate_dsq(kaola_rate_14.config.type, str(int(others().randomString())),kaola_rate_14.config.from_system, str(datetime.date.today()), '110000', 1,kaola_rate_14.config.product_number)
        if rsp.code == 0:
            print 'rsp.code != 0,Error'
        else:
            self.assertEqual(rsp.data['calculate_result']['grant']['amount'], 110000)
            self.assertEqual(rsp.data['calculate_result']['grant']['period'], 0)
            self.assertEqual(rsp.data['calculate_result']['grant']['date'], str(datetime.date.today()))
            self.assertEqual(rsp.data['calculate_result']['principal'][0]['amount'], 110000)
            self.assertEqual(rsp.data['calculate_result']['principal'][0]['date'], kaola_rate_14.date)
            self.assertEqual(rsp.data['calculate_result']['principal'][0]['period'], 1)
            self.assertEqual(rsp.data['calculate_result']['interest'][0]['date'], kaola_rate_14.date)
            self.assertEqual(rsp.data['calculate_result']['interest'][0]['amount'], obj.calcRuleOne())
            self.assertEqual(rsp.data['calculate_result']['fee']['service'][0]['repay_type'], 'ending_deduction')
            self.assertEqual(rsp.data['calculate_result']['fee']['service'][0]['period'], 1)
            self.assertEqual(rsp.data['calculate_result']['fee']['service'][0]['date'], kaola_rate_14.date)
            self.assertEqual(rsp.data['calculate_result']['fee']['service'][0]['amount'], obj.calcRuleTwo())
            self.assertEqual(rsp.data['calculate_result']['fee']['audit'][0]['repay_type'], 'ending_deduction')
            self.assertEqual(rsp.data['calculate_result']['fee']['audit'][0]['period'], 1)
            self.assertEqual(rsp.data['calculate_result']['fee']['audit'][0]['date'], kaola_rate_14.date)
            self.assertEqual(rsp.data['calculate_result']['fee']['audit'][0]['amount'], int(self.config.auditfee))

    def test_kaola_rate_14_1200(self):
        # 创建接口模型对象
        calconfig = rateSystem()
        # 计算服务费和利息
        obj = rateCalcRule(120000, kaola_rate_14.config.interestrate, kaola_rate_14.config.expenses, kaola_rate_14.config.countdays,kaola_rate_14.config.borrowdays)
        # 准备响应体参数
        rsp = calconfig.calculate_dsq(kaola_rate_14.config.type, str(int(others().randomString())),kaola_rate_14.config.from_system, str(datetime.date.today()), '120000', 1,kaola_rate_14.config.product_number)
        if rsp.code == 0:
            print 'rsp.code != 0,Error'
        else:
            self.assertEqual(rsp.data['calculate_result']['grant']['amount'], 120000)
            self.assertEqual(rsp.data['calculate_result']['grant']['period'], 0)
            self.assertEqual(rsp.data['calculate_result']['grant']['date'], str(datetime.date.today()))
            self.assertEqual(rsp.data['calculate_result']['principal'][0]['amount'], 120000)
            self.assertEqual(rsp.data['calculate_result']['principal'][0]['date'], kaola_rate_14.date)
            self.assertEqual(rsp.data['calculate_result']['principal'][0]['period'], 1)
            self.assertEqual(rsp.data['calculate_result']['interest'][0]['date'], kaola_rate_14.date)
            self.assertEqual(rsp.data['calculate_result']['interest'][0]['amount'], obj.calcRuleOne())
            self.assertEqual(rsp.data['calculate_result']['fee']['service'][0]['repay_type'], 'ending_deduction')
            self.assertEqual(rsp.data['calculate_result']['fee']['service'][0]['period'], 1)
            self.assertEqual(rsp.data['calculate_result']['fee']['service'][0]['date'], kaola_rate_14.date)
            self.assertEqual(rsp.data['calculate_result']['fee']['service'][0]['amount'], obj.calcRuleTwo())
            self.assertEqual(rsp.data['calculate_result']['fee']['audit'][0]['repay_type'], 'ending_deduction')
            self.assertEqual(rsp.data['calculate_result']['fee']['audit'][0]['period'], 1)
            self.assertEqual(rsp.data['calculate_result']['fee']['audit'][0]['date'], kaola_rate_14.date)
            self.assertEqual(rsp.data['calculate_result']['fee']['audit'][0]['amount'], int(self.config.auditfee))

    def test_kaola_rate_14_1300(self):
        # 创建接口模型对象
        calconfig = rateSystem()
        # 计算服务费和利息
        obj = rateCalcRule(130000, kaola_rate_14.config.interestrate, kaola_rate_14.config.expenses, kaola_rate_14.config.countdays,kaola_rate_14.config.borrowdays)
        # 准备响应体参数
        rsp = calconfig.calculate_dsq(kaola_rate_14.config.type, str(int(others().randomString())),kaola_rate_14.config.from_system, str(datetime.date.today()), '130000', 1,kaola_rate_14.config.product_number)
        if rsp.code == 0:
            print 'rsp.code != 0,Error'
        else:
            self.assertEqual(rsp.data['calculate_result']['grant']['amount'], 130000)
            self.assertEqual(rsp.data['calculate_result']['grant']['period'], 0)
            self.assertEqual(rsp.data['calculate_result']['grant']['date'], str(datetime.date.today()))
            self.assertEqual(rsp.data['calculate_result']['principal'][0]['amount'], 130000)
            self.assertEqual(rsp.data['calculate_result']['principal'][0]['date'], kaola_rate_14.date)
            self.assertEqual(rsp.data['calculate_result']['principal'][0]['period'], 1)
            self.assertEqual(rsp.data['calculate_result']['interest'][0]['date'], kaola_rate_14.date)
            self.assertEqual(rsp.data['calculate_result']['interest'][0]['amount'], obj.calcRuleOne())
            self.assertEqual(rsp.data['calculate_result']['fee']['service'][0]['repay_type'], 'ending_deduction')
            self.assertEqual(rsp.data['calculate_result']['fee']['service'][0]['period'], 1)
            self.assertEqual(rsp.data['calculate_result']['fee']['service'][0]['date'], kaola_rate_14.date)
            self.assertEqual(rsp.data['calculate_result']['fee']['service'][0]['amount'], obj.calcRuleTwo())
            self.assertEqual(rsp.data['calculate_result']['fee']['audit'][0]['repay_type'], 'ending_deduction')
            self.assertEqual(rsp.data['calculate_result']['fee']['audit'][0]['period'], 1)
            self.assertEqual(rsp.data['calculate_result']['fee']['audit'][0]['date'], kaola_rate_14.date)
            self.assertEqual(rsp.data['calculate_result']['fee']['audit'][0]['amount'], int(self.config.auditfee))

    def test_kaola_rate_14_1400(self):
        # 创建接口模型对象
        calconfig = rateSystem()
        # 计算服务费和利息
        obj = rateCalcRule(140000, kaola_rate_14.config.interestrate, kaola_rate_14.config.expenses, kaola_rate_14.config.countdays,kaola_rate_14.config.borrowdays)
        # 准备响应体参数
        rsp = calconfig.calculate_dsq(kaola_rate_14.config.type, str(int(others().randomString())),kaola_rate_14.config.from_system, str(datetime.date.today()), '140000', 1,kaola_rate_14.config.product_number)
        if rsp.code == 0:
            print 'rsp.code != 0,Error'
        else:
            self.assertEqual(rsp.data['calculate_result']['grant']['amount'], 140000)
            self.assertEqual(rsp.data['calculate_result']['grant']['period'], 0)
            self.assertEqual(rsp.data['calculate_result']['grant']['date'], str(datetime.date.today()))
            self.assertEqual(rsp.data['calculate_result']['principal'][0]['amount'], 140000)
            self.assertEqual(rsp.data['calculate_result']['principal'][0]['date'], kaola_rate_14.date)
            self.assertEqual(rsp.data['calculate_result']['principal'][0]['period'], 1)
            self.assertEqual(rsp.data['calculate_result']['interest'][0]['date'], kaola_rate_14.date)
            self.assertEqual(rsp.data['calculate_result']['interest'][0]['amount'], obj.calcRuleOne())
            self.assertEqual(rsp.data['calculate_result']['fee']['service'][0]['repay_type'], 'ending_deduction')
            self.assertEqual(rsp.data['calculate_result']['fee']['service'][0]['period'], 1)
            self.assertEqual(rsp.data['calculate_result']['fee']['service'][0]['date'], kaola_rate_14.date)
            self.assertEqual(rsp.data['calculate_result']['fee']['service'][0]['amount'], obj.calcRuleTwo())
            self.assertEqual(rsp.data['calculate_result']['fee']['audit'][0]['repay_type'], 'ending_deduction')
            self.assertEqual(rsp.data['calculate_result']['fee']['audit'][0]['period'], 1)
            self.assertEqual(rsp.data['calculate_result']['fee']['audit'][0]['date'], kaola_rate_14.date)
            self.assertEqual(rsp.data['calculate_result']['fee']['audit'][0]['amount'], int(self.config.auditfee))

    def test_kaola_rate_14_1500(self):
        # 创建接口模型对象
        calconfig = rateSystem()
        # 计算服务费和利息
        obj = rateCalcRule(150000, kaola_rate_14.config.interestrate, kaola_rate_14.config.expenses, kaola_rate_14.config.countdays,kaola_rate_14.config.borrowdays)
        # 准备响应体参数
        rsp = calconfig.calculate_dsq(kaola_rate_14.config.type, str(int(others().randomString())),kaola_rate_14.config.from_system, str(datetime.date.today()), '150000', 1,kaola_rate_14.config.product_number)
        if rsp.code == 0:
            print 'rsp.code != 0,Error'
        else:
            self.assertEqual(rsp.data['calculate_result']['grant']['amount'], 150000)
            self.assertEqual(rsp.data['calculate_result']['grant']['period'], 0)
            self.assertEqual(rsp.data['calculate_result']['grant']['date'], str(datetime.date.today()))
            self.assertEqual(rsp.data['calculate_result']['principal'][0]['amount'], 150000)
            self.assertEqual(rsp.data['calculate_result']['principal'][0]['date'], kaola_rate_14.date)
            self.assertEqual(rsp.data['calculate_result']['principal'][0]['period'], 1)
            self.assertEqual(rsp.data['calculate_result']['interest'][0]['date'], kaola_rate_14.date)
            self.assertEqual(rsp.data['calculate_result']['interest'][0]['amount'], obj.calcRuleOne())
            self.assertEqual(rsp.data['calculate_result']['fee']['service'][0]['repay_type'], 'ending_deduction')
            self.assertEqual(rsp.data['calculate_result']['fee']['service'][0]['period'], 1)
            self.assertEqual(rsp.data['calculate_result']['fee']['service'][0]['date'], kaola_rate_14.date)
            self.assertEqual(rsp.data['calculate_result']['fee']['service'][0]['amount'], obj.calcRuleTwo())
            self.assertEqual(rsp.data['calculate_result']['fee']['audit'][0]['repay_type'], 'ending_deduction')
            self.assertEqual(rsp.data['calculate_result']['fee']['audit'][0]['period'], 1)
            self.assertEqual(rsp.data['calculate_result']['fee']['audit'][0]['date'], kaola_rate_14.date)
            self.assertEqual(rsp.data['calculate_result']['fee']['audit'][0]['amount'], int(self.config.auditfee))

    def test_kaola_rate_14_1600(self):
        # 创建接口模型对象
        calconfig = rateSystem()
        # 计算服务费和利息
        obj = rateCalcRule(160000, kaola_rate_14.config.interestrate, kaola_rate_14.config.expenses, kaola_rate_14.config.countdays,kaola_rate_14.config.borrowdays)
        # 准备响应体参数
        rsp = calconfig.calculate_dsq(kaola_rate_14.config.type, str(int(others().randomString())),kaola_rate_14.config.from_system, str(datetime.date.today()), '160000', 1,kaola_rate_14.config.product_number)
        if rsp.code == 0:
            print 'rsp.code != 0,Error'
        else:
            self.assertEqual(rsp.data['calculate_result']['grant']['amount'], 160000)
            self.assertEqual(rsp.data['calculate_result']['grant']['period'], 0)
            self.assertEqual(rsp.data['calculate_result']['grant']['date'], str(datetime.date.today()))
            self.assertEqual(rsp.data['calculate_result']['principal'][0]['amount'], 160000)
            self.assertEqual(rsp.data['calculate_result']['principal'][0]['date'], kaola_rate_14.date)
            self.assertEqual(rsp.data['calculate_result']['principal'][0]['period'], 1)
            self.assertEqual(rsp.data['calculate_result']['interest'][0]['date'], kaola_rate_14.date)
            self.assertEqual(rsp.data['calculate_result']['interest'][0]['amount'], obj.calcRuleOne())
            self.assertEqual(rsp.data['calculate_result']['fee']['service'][0]['repay_type'], 'ending_deduction')
            self.assertEqual(rsp.data['calculate_result']['fee']['service'][0]['period'], 1)
            self.assertEqual(rsp.data['calculate_result']['fee']['service'][0]['date'], kaola_rate_14.date)
            self.assertEqual(rsp.data['calculate_result']['fee']['service'][0]['amount'], obj.calcRuleTwo())
            self.assertEqual(rsp.data['calculate_result']['fee']['audit'][0]['repay_type'], 'ending_deduction')
            self.assertEqual(rsp.data['calculate_result']['fee']['audit'][0]['period'], 1)
            self.assertEqual(rsp.data['calculate_result']['fee']['audit'][0]['date'], kaola_rate_14.date)
            self.assertEqual(rsp.data['calculate_result']['fee']['audit'][0]['amount'], int(self.config.auditfee))

    def test_kaola_rate_14_1700(self):
        # 创建接口模型对象
        calconfig = rateSystem()
        # 计算服务费和利息
        obj = rateCalcRule(170000, kaola_rate_14.config.interestrate, kaola_rate_14.config.expenses, kaola_rate_14.config.countdays,kaola_rate_14.config.borrowdays)
        # 准备响应体参数
        rsp = calconfig.calculate_dsq(kaola_rate_14.config.type, str(int(others().randomString())),kaola_rate_14.config.from_system, str(datetime.date.today()), '170000', 1,kaola_rate_14.config.product_number)
        if rsp.code == 0:
            print 'rsp.code != 0,Error'
        else:
            self.assertEqual(rsp.data['calculate_result']['grant']['amount'], 170000)
            self.assertEqual(rsp.data['calculate_result']['grant']['period'], 0)
            self.assertEqual(rsp.data['calculate_result']['grant']['date'], str(datetime.date.today()))
            self.assertEqual(rsp.data['calculate_result']['principal'][0]['amount'], 170000)
            self.assertEqual(rsp.data['calculate_result']['principal'][0]['date'], kaola_rate_14.date)
            self.assertEqual(rsp.data['calculate_result']['principal'][0]['period'], 1)
            self.assertEqual(rsp.data['calculate_result']['interest'][0]['date'], kaola_rate_14.date)
            self.assertEqual(rsp.data['calculate_result']['interest'][0]['amount'], obj.calcRuleOne())
            self.assertEqual(rsp.data['calculate_result']['fee']['service'][0]['repay_type'], 'ending_deduction')
            self.assertEqual(rsp.data['calculate_result']['fee']['service'][0]['period'], 1)
            self.assertEqual(rsp.data['calculate_result']['fee']['service'][0]['date'], kaola_rate_14.date)
            self.assertEqual(rsp.data['calculate_result']['fee']['service'][0]['amount'], obj.calcRuleTwo())
            self.assertEqual(rsp.data['calculate_result']['fee']['audit'][0]['repay_type'], 'ending_deduction')
            self.assertEqual(rsp.data['calculate_result']['fee']['audit'][0]['period'], 1)
            self.assertEqual(rsp.data['calculate_result']['fee']['audit'][0]['date'], kaola_rate_14.date)
            self.assertEqual(rsp.data['calculate_result']['fee']['audit'][0]['amount'], int(self.config.auditfee))

    def test_kaola_rate_14_1800(self):
        # 创建接口模型对象
        calconfig = rateSystem()
        # 计算服务费和利息
        obj = rateCalcRule(180000, kaola_rate_14.config.interestrate, kaola_rate_14.config.expenses, kaola_rate_14.config.countdays,kaola_rate_14.config.borrowdays)
        # 准备响应体参数
        rsp = calconfig.calculate_dsq(kaola_rate_14.config.type, str(int(others().randomString())),kaola_rate_14.config.from_system, str(datetime.date.today()), '180000', 1,kaola_rate_14.config.product_number)
        if rsp.code == 0:
            print 'rsp.code != 0,Error'
        else:
            self.assertEqual(rsp.data['calculate_result']['grant']['amount'], 180000)
            self.assertEqual(rsp.data['calculate_result']['grant']['period'], 0)
            self.assertEqual(rsp.data['calculate_result']['grant']['date'], str(datetime.date.today()))
            self.assertEqual(rsp.data['calculate_result']['principal'][0]['amount'], 180000)
            self.assertEqual(rsp.data['calculate_result']['principal'][0]['date'], kaola_rate_14.date)
            self.assertEqual(rsp.data['calculate_result']['principal'][0]['period'], 1)
            self.assertEqual(rsp.data['calculate_result']['interest'][0]['date'], kaola_rate_14.date)
            self.assertEqual(rsp.data['calculate_result']['interest'][0]['amount'], obj.calcRuleOne())
            self.assertEqual(rsp.data['calculate_result']['fee']['service'][0]['repay_type'], 'ending_deduction')
            self.assertEqual(rsp.data['calculate_result']['fee']['service'][0]['period'], 1)
            self.assertEqual(rsp.data['calculate_result']['fee']['service'][0]['date'], kaola_rate_14.date)
            self.assertEqual(rsp.data['calculate_result']['fee']['service'][0]['amount'], obj.calcRuleTwo())
            self.assertEqual(rsp.data['calculate_result']['fee']['audit'][0]['repay_type'], 'ending_deduction')
            self.assertEqual(rsp.data['calculate_result']['fee']['audit'][0]['period'], 1)
            self.assertEqual(rsp.data['calculate_result']['fee']['audit'][0]['date'], kaola_rate_14.date)
            self.assertEqual(rsp.data['calculate_result']['fee']['audit'][0]['amount'], int(self.config.auditfee))

    def test_kaola_rate_14_1900(self):
        # 创建接口模型对象
        calconfig = rateSystem()
        # 计算服务费和利息
        obj = rateCalcRule(190000, kaola_rate_14.config.interestrate, kaola_rate_14.config.expenses, kaola_rate_14.config.countdays,kaola_rate_14.config.borrowdays)
        # 准备响应体参数
        rsp = calconfig.calculate_dsq(kaola_rate_14.config.type, str(int(others().randomString())),kaola_rate_14.config.from_system, str(datetime.date.today()), '190000', 1,kaola_rate_14.config.product_number)
        if rsp.code == 0:
            print 'rsp.code != 0,Error'
        else:
            self.assertEqual(rsp.data['calculate_result']['grant']['amount'], 190000)
            self.assertEqual(rsp.data['calculate_result']['grant']['period'], 0)
            self.assertEqual(rsp.data['calculate_result']['grant']['date'], str(datetime.date.today()))
            self.assertEqual(rsp.data['calculate_result']['principal'][0]['amount'], 190000)
            self.assertEqual(rsp.data['calculate_result']['principal'][0]['date'], kaola_rate_14.date)
            self.assertEqual(rsp.data['calculate_result']['principal'][0]['period'], 1)
            self.assertEqual(rsp.data['calculate_result']['interest'][0]['date'], kaola_rate_14.date)
            self.assertEqual(rsp.data['calculate_result']['interest'][0]['amount'], obj.calcRuleOne())
            self.assertEqual(rsp.data['calculate_result']['fee']['service'][0]['repay_type'], 'ending_deduction')
            self.assertEqual(rsp.data['calculate_result']['fee']['service'][0]['period'], 1)
            self.assertEqual(rsp.data['calculate_result']['fee']['service'][0]['date'], kaola_rate_14.date)
            self.assertEqual(rsp.data['calculate_result']['fee']['service'][0]['amount'], obj.calcRuleTwo())
            self.assertEqual(rsp.data['calculate_result']['fee']['audit'][0]['repay_type'], 'ending_deduction')
            self.assertEqual(rsp.data['calculate_result']['fee']['audit'][0]['period'], 1)
            self.assertEqual(rsp.data['calculate_result']['fee']['audit'][0]['date'], kaola_rate_14.date)
            self.assertEqual(rsp.data['calculate_result']['fee']['audit'][0]['amount'], int(self.config.auditfee))

    def test_kaola_rate_14_2000(self):
        # 创建接口模型对象
        calconfig = rateSystem()
        # 计算服务费和利息
        obj = rateCalcRule(200000, kaola_rate_14.config.interestrate, kaola_rate_14.config.expenses, kaola_rate_14.config.countdays,kaola_rate_14.config.borrowdays)
        # 准备响应体参数
        rsp = calconfig.calculate_dsq(kaola_rate_14.config.type, str(int(others().randomString())),kaola_rate_14.config.from_system, str(datetime.date.today()), '200000', 1,kaola_rate_14.config.product_number)
        if rsp.code == 0:
            print 'rsp.code != 0,Error'
        else:
            self.assertEqual(rsp.data['calculate_result']['grant']['amount'], 200000)
            self.assertEqual(rsp.data['calculate_result']['grant']['period'], 0)
            self.assertEqual(rsp.data['calculate_result']['grant']['date'], str(datetime.date.today()))
            self.assertEqual(rsp.data['calculate_result']['principal'][0]['amount'], 200000)
            self.assertEqual(rsp.data['calculate_result']['principal'][0]['date'], kaola_rate_14.date)
            self.assertEqual(rsp.data['calculate_result']['principal'][0]['period'], 1)
            self.assertEqual(rsp.data['calculate_result']['interest'][0]['date'], kaola_rate_14.date)
            self.assertEqual(rsp.data['calculate_result']['interest'][0]['amount'], obj.calcRuleOne())
            self.assertEqual(rsp.data['calculate_result']['fee']['service'][0]['repay_type'], 'ending_deduction')
            self.assertEqual(rsp.data['calculate_result']['fee']['service'][0]['period'], 1)
            self.assertEqual(rsp.data['calculate_result']['fee']['service'][0]['date'], kaola_rate_14.date)
            self.assertEqual(rsp.data['calculate_result']['fee']['service'][0]['amount'], obj.calcRuleTwo())
            self.assertEqual(rsp.data['calculate_result']['fee']['audit'][0]['repay_type'], 'ending_deduction')
            self.assertEqual(rsp.data['calculate_result']['fee']['audit'][0]['period'], 1)
            self.assertEqual(rsp.data['calculate_result']['fee']['audit'][0]['date'], kaola_rate_14.date)
            self.assertEqual(rsp.data['calculate_result']['fee']['audit'][0]['amount'], int(self.config.auditfee))

def suite ():
    suite = unittest.TestSuite()
    suite.addTest(kaola_rate_14("test_kaola_rate_14_500"))
    suite.addTest(kaola_rate_14("test_kaola_rate_14_600"))
    suite.addTest(kaola_rate_14("test_kaola_rate_14_700"))
    suite.addTest(kaola_rate_14("test_kaola_rate_14_800"))
    suite.addTest(kaola_rate_14("test_kaola_rate_14_900"))
    suite.addTest(kaola_rate_14("test_kaola_rate_14_1000"))
    suite.addTest(kaola_rate_14("test_kaola_rate_14_1100"))
    suite.addTest(kaola_rate_14("test_kaola_rate_14_1200"))
    suite.addTest(kaola_rate_14("test_kaola_rate_14_1300"))
    suite.addTest(kaola_rate_14("test_kaola_rate_14_1400"))
    suite.addTest(kaola_rate_14("test_kaola_rate_14_1500"))
    suite.addTest(kaola_rate_14("test_kaola_rate_14_1600"))
    suite.addTest(kaola_rate_14("test_kaola_rate_14_1700"))
    suite.addTest(kaola_rate_14("test_kaola_rate_14_1800"))
    suite.addTest(kaola_rate_14("test_kaola_rate_14_1900"))
    suite.addTest(kaola_rate_14("test_kaola_rate_14_2000"))
    return suite