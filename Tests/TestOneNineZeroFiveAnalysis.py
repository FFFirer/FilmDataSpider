# -*- coding:utf-8 -*-

import sys
sys.path.append('E:\CodeRepos\FilmDataSpider')
import HtmlAnalysises.OneNineZeroFiveAnalysis
import Spiders.MySpider

def Test1():
    test_page = Spiders.MySpider.GetHtmlWithHeader('https://www.1905.com/mdb/film/224/info/')
    summary = HtmlAnalysises.OneNineZeroFiveAnalysis.GetFilmSummary(test_page)

    print('success')

if __name__ == "__main__":
    Test1()