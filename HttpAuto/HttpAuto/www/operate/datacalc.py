#! /usr/bin/env python
# -*- coding:utf-8 -*-

import time,datetime

'''
Package the rate calculate api

Author by slyutae on 2017.09.09
'''

class datecalculate:

    def __init__(self,delta):
        self.delta = delta


    def datecalc(self):
        self.date = datetime.date.today()
        time1 = self.date + datetime.timedelta(days = self.delta)
        returndate = datetime.date.strftime(time1,'%Y-%m-%d')
        return returndate

if __name__ == '__main__':
    a = datecalculate(1).datecalc()
    print a