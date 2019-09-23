# -*- coding:utf-8 -*-

import time
import sys
sys.path.append('E:\CodeRepos\FilmDataSpider')
import LogCenter

thislog = LogCenter.logger

while True:
    time.sleep(1)
    thislog.info('a info thing')
    thislog.warn('a warn thing')
    thislog.error('a error thing')