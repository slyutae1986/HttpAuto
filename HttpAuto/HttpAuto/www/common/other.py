#! /usr/bin/env python
# -*- coding:utf-8 -*-


"""
package some func like

Author by slyutae on 2017/09/06

"""

import random
import time,datetime


class others:

    def randomString(self):
        tup = (1000,9999)
        basestr = random.randint(tup[0],tup[1])
        timestr = time.time()
        return basestr+timestr


class Dict(dict):

    def __init__(self,key = (),values = (),**kw):
        super(Dict,self).__init__(*kw)
        for k,a in zip(key,values):
            self[k] = a

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise  AttributeError(r"'Dict' object has no atrribute '%s'" %key)

    def __setattr__(self, key, value):
        self[key] = value
