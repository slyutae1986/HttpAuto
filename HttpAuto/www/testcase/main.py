#! /usr/bin/env python
# -*- Coding:utf-8 -*-

import unittest
from www.common.database import *



"""
runner is here,write the test suite runner here

Author by slyutae
"""



if __name__ == '__main__':

    create_engine()

    runner = unittest.TextTestRunner()

    from www.testcase.ts_rate_calculate import verifyRateCaculate
    runner.run(verifyRateCaculate.suite())