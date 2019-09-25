# -*- coding:utf-8 -*-

import requests
import OneNineZeroFiveAnalysis
import OneNineZeroFiveDbService
import LogCenter
import ConfigHelper
import time

Headers1 = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Language': 'zh,zh-TW;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6',
            'Connection': 'keep-alive'}


logger = LogCenter.logger

# 初始化网站根链接
def InitBaseConfig(website_root):
    ConfigHelper.root_url = website_root

# 返回utf8编码的html
def GetHtml(url):
    origin_html = requests.get(url)
    return origin_html.text

# 1905网的Header
def GetHtmlWithHeader(url):
    origin_html = requests.get(url, headers=Headers1)
    return origin_html.text

# 获取url页面上的所有影片-1905
def GetFilmsOnPage(url):
    Page_Content = GetHtmlWithHeader(url)
    # 获取当前所有影片连接
    All_URLs=OneNineZeroFiveAnalysis.GetAllFilmeLinkOnPage(Page_Content)
    for url in All_URLs:
        sections = url.split('/')
        filmId = sections[-2]
        exist=OneNineZeroFiveDbService.QueryFilmExists(filmId)
        logger.info(str.format('%s, Exist? %s' % (url, exist)))
        if(not exist):
            CurrentFilmPageContent = GetHtmlWithHeader(ConfigHelper.root_url + url + 'info/')
            summary = OneNineZeroFiveAnalysis.GetFilmSummary(CurrentFilmPageContent)
            # 存入数据库
            OneNineZeroFiveDbService.InsertData(summary, filmId)
            logger.info(str.format('Save Success! %s' % summary))
    # 查找下一个链接
    NextPage_Url = OneNineZeroFiveAnalysis.GetNextPageUrl(Page_Content)
    if(len(NextPage_Url)>0):
        Full_NextPage_Url = ConfigHelper.root_url + NextPage_Url
        logger.info(str.format('goto %s' % (Full_NextPage_Url)))
        time.sleep(2)
        GetFilmsOnPage(Full_NextPage_Url)
