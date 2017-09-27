#! /usr/bin/env python
# -*- coding:utf-8 -*-

"""
waiting for a moment

Author by slyutae

"""

import configparser


class config:

    def __init__(self,ini_file = '../../config/env_config.ini'):
        ini_file = '../../config/env_config.ini'
        configEnv = configparser.ConfigParser()
        configEnv.read(ini_file)
        self.envName = configEnv['ENV']['env']
        self.configHttp = self.getconfig(envName= self.envName,iniName='../../config/Http_config.ini')
        self.configserver = self.getconfig(envName = self.envName,iniName='../../config/server_config.ini')
        self.configDB = self.getconfig(envName = self.envName,iniName='../../config/db_config.ini')

    def getconfig(self,envName,iniName):
        config = configparser.ConfigParser()
        config.read(iniName)
        keys = config.options(envName)
        values = []
        for i in range(0,len(keys)):
            values.append(config.get(envName,keys[i]))
        from other import Dict
        return Dict(keys,values)