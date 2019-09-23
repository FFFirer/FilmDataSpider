# -*- coding:utf-8 -*-

# 导入包
import Spiders.MySpider
import sys
sys.path.append('E:\CodeRepos\FilmDataSpider')
import DbServices.OneNineZeroFiveDbService
import HtmlAnalysises.OneNineZeroFiveAnalysis
import LogCenter

# 主程序
def main():
    origin = Spiders.MySpider.GetHtml(r'https://www.1905.com/mdb/film/2246406/info/')
    data = HtmlAnalysises.OneNineZeroFiveAnalysis.GetFilmSummary(origin)
    DbServices.OneNineZeroFiveDbService.HandleData(data, '2246406')

    LogCenter.logger.info('success')

# 执行程序
if __name__ == "__main__":
    main()