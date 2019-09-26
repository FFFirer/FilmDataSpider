# -*- coding:utf-8 -*-

import requests
from lxml import etree
import OneNineZeroFiveAnalysis
import MySpider



def GetNextPageUrlTest():
    page = MySpider.GetHtmlWithHeader('https://www.1905.com/mdb/film/list/enindex-A/')
    next_url = OneNineZeroFiveAnalysis.GetNextPageUrl(page)


def GetFilmSummaryTest():
    page = MySpider.GetHtmlWithHeader('https://www.1905.com/mdb/film/2246987/info/')
    summary = OneNineZeroFiveAnalysis.GetFilmSummary(page)



if __name__ == "__main__":
    #GetNextPageUrlTest()
    GetFilmSummaryTest()