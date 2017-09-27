#! usr/bin/env python
# -*- coding:utf-8 -*-

"""
Package the rate calculate api

Author by slyutae on 2017.09.09

"""


import xlwings as xw
from www.common.other import Dict
import os



ratedata_path = r'C:\Users\dell-pc\Desktop\HttpAuto\testdata\ratedata.xlsx'


def rData(sheetname):
    wb = xw.Book(ratedata_path).sheets[sheetname]
    length = wb.range(1, 1).expand().shape
    excelData = Dict()
    for i in range(2,length[0]):
        keys = wb.range('A'+str(i)).value
        values = wb.range('B'+str(i)).value
        if values is not None and values != '':
            if  values[0] == '['and values[-1] == ']':
                 excelData[keys] = eval(values)
            elif '{' in values and '}' in values:
                dictData = eval(values.encode('utf-8'))
                dictkeys = []
                dictvalues = []
                for (k,v) in dictData.interitems:
                    dictkeys.append(k)
                    dictvalues.append(v)
                excelData[keys] = Dict(dictkeys,dictvalues)
            else:
                excelData[keys] = values.encode('utf-8')
        elif values == '':
          excelData[keys] = ''
    return excelData

if __name__ == '__main__':
    teststr = rData('dsq_kaola_14')
    print teststr