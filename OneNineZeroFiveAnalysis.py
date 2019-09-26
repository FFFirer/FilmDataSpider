# -*- coding:utf-8 -*-

from lxml import etree
import re
import LogCenter

# 获取电影链接
# def GetFilmLink(html_content):
#     html_object = etree.HTML(html_content)
#     target_link = html_object.xpath('//*[@id="filmSearch"]/div[1]/a/@href')
#     return target_link

p_shootingInfo=r'<!-- <ul class="clearfloat">(.*?)</ul> -->'
logger = LogCenter.logger

# 获取电影信息
def GetFilmSummary(film_page):
    html = etree.HTML(film_page)
    FilmName = html.xpath('//dt[text()="片\xa0\xa0\xa0\xa0\xa0\xa0\xa0名"]/following-sibling::dd[1]/text()')
    Country = html.xpath('//dt[text()="国\xa0\xa0\xa0\xa0\xa0\xa0\xa0别"]/following-sibling::dd[1]/text()')
    Language = html.xpath('//dt[text()="语\xa0\xa0\xa0\xa0\xa0\xa0\xa0言"]/following-sibling::dd[1]/text()')
    FilmType = html.xpath('//dt[text()="影片类型"]/following-sibling::dd[1]/text()')
    OtherCNFilmName = html.xpath('//dt[text()="更多中文名"]/following-sibling::dd[1]/p/text()')
    OtherENFilmName = html.xpath('//dt[text()="更多外文名"]/following-sibling::dd[1]/p/text()')
    PlayTime = html.xpath('//dt[text()="时\xa0\xa0\xa0\xa0\xa0\xa0\xa0长"]/following-sibling::dd[1]/text()')
    Color = html.xpath('//dt[text()="色\xa0\xa0\xa0\xa0\xa0\xa0\xa0彩"]/following-sibling::dd[1]/text()')
    PlayType = html.xpath('//dt[text()="版\xa0\xa0\xa0\xa0\xa0\xa0\xa0本"]/following-sibling::dd[1]/text()')
    PlayInfo = html.xpath('//dt[text()="上映信息"]/following-sibling::dd[1]/p/text()')
    UserRating = html.xpath('//dt[text()="用户评分"]/following-sibling::dd[1]/text()')
    
    temp = [FilmName, Country, Language, FilmType, OtherCNFilmName, OtherENFilmName, PlayTime, Color, PlayType, PlayInfo, UserRating]

    # 通过正则获取注释掉的内容
    zhushi_html = re.findall(p_shootingInfo, film_page, re.S|re.M)
    if(len(zhushi_html) > 0):
        html2 = etree.HTML(zhushi_html[0])
        ShootingTime = html2.xpath('//dt[text()="拍摄日期"]/following-sibling::dd[1]/text()')
        FilmingLocations = html2.xpath('//dt[text()="拍\xa0\xa0摄\xa0\xa0地"]/following-sibling::dd[1]/text()')
        temp.append(ShootingTime)
        temp.append(FilmingLocations)
    else:
        temp.append([])
        temp.append([])

    summary = []
    for i in range(len(temp)):
        if(len(temp[i])>0):
            summary.append(','.join(tuple(temp[i])))
            summary[i] = summary[i].replace('\xa0\xa0\xa0', '/')
            summary[i] = summary[i].replace('\xa0\xa0', '/')
            summary[i] = summary[i].replace('\xa0', '')
            
            summary[i] = summary[i].strip('/')
            if(len(summary[i])>4000):
                logger.warn(str.format('字段数据超过长度限制4000,pos[%d],%s' % (i, summary[i])))
            #     summary[i] = summary[i][:255]
        else:
            summary.append('') 

    return summary


# 获取下一页链接
def GetNextPageUrl(page_content):
    html = etree.HTML(page_content)
    #nextpage_url = html.xpath('//*[@id="new_page"]/a[5]/@href')
    nextpage_url = html.xpath('//a[text()="下一页"]/@href')
    return nextpage_url[0]

# 获取当前页面所有影片的链接
def GetAllFilmeLinkOnPage(page_content):
    html = etree.HTML(page_content)
    film_urls = html.xpath('/html/body/div[2]/div[1]/ul/li/a/@href')

    #print(film_urls)

    return film_urls


def GetContentTest(page_content):
    html = etree.HTML(page_content)
    res = html.xpath(r'/html/body/section[3]/div/ul/li/div[2]/ul[2]/dl[1]/dt/text()')
    #res = html.xpath('//dt[text()="色\xa0\xa0\xa0\xa0\xa0\xa0\xa0彩"]/text()')
    return res