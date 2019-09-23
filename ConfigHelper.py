# -*- coding:utf-8 -*-
import configparser
import os,sys

conf = configparser.ConfigParser()
confile = open('conf.ini')
conf.readfp(confile)

SqlServerHost = conf.get('sqlserver', 'SqlServerHost')
SqlServerUser = conf.get('sqlserver', 'SqlServerUser')
SqlServerPwd = conf.get('sqlserver', 'SqlServerPwd')
DbName = conf.get('sqlserver', 'DbName')