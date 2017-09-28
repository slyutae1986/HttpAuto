#! /usr/bin/env python
# -*- coding:utf-8 -*-

"""
requests is a simple framework

Author by slyutae

"""



import requests,json
from www.common.config import config
from www.common.other import Dict




class httpbase:

    def __init__(self):
        httpbase = config().configHttp
        self.name = httpbase['testing_name']
        self.host = httpbase['testing_host']
        self.port = httpbase['testing_port']
        self.header = {"Content-Type":"application/json"}
        self.body ={}


    def sendJsonPost(self,data = None,url = None):
        urlpost = 'http://' + self.host + ':' + str(self.port) + url
        params = json.dumps(data, encoding="UTF-8", ensure_ascii=False)
        try:
            rsppost = requests.post(urlpost,data = params,headers = self.header)
            dict = json.loads(rsppost.content)
            for key,values in dict.iteritems():
                self.body[key] = values
            self.body =Dict(self.body.keys(),self.body.values())
            return self.body
        except Exception as e:
            print('%s' %e)
            return {}

    def sendget(self,url = None,params = None):
        urlget = 'http://'+str(self.host)+':'+str(self.port)+str(url)
        data = params
        try:
            rspget = requests.get(urlget,data)
            json = rspget.json()
            return json
        except Exception as d:
            print('%s' %d)
            return {}

if __name__ == '__main__':
    A = httpbase()
    data = {'data': {'apply_amount': '50000','sign_date': '2017-09-28','product_number': 'paydayloan_kaola_14_20170822010442',
    'period_count': 1},'type': 'CalculateRepayPlan','key': '1506587026','from_system': 'DSQ'}
    url = '/v5/rate/calculate'
    A.sendJsonPost(data,url)