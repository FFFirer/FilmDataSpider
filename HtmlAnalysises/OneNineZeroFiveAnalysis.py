# -*- coding:utf-8 -*-

from lxml import etree

# 获取电影链接
def GetFilmLink(html_content):
    html_object = etree.HTML(html_content)
    target_link = html_object.xpath('//*[@id="filmSearch"]/div[1]/a/@href')
    return target_link

def GetFilmSummary(film_page):
    html = etree.HTML(film_page)
    FilmName = html.xpath('/html/body/section[3]/div/ul/li/div[1]/dl[1]/dd/text()')
    Country = html.xpath('/html/body/section[3]/div/ul/li/div[1]/ul[2]/dl[1]/dd/text()')
    Language = html.xpath('/html/body/section[3]/div/ul/li/div[1]/ul[2]/dl[2]/dd/text()')
    FilmType = html.xpath('/html/body/section[3]/div/ul/li/div[1]/ul[3]/dl/dd/text()')
    OtherFilmName = html.xpath('/html/body/section[3]/div/ul/li/div[1]/ul[4]/dl/dd/*/text()')
    PlayTime = html.xpath('/html/body/section[3]/div/ul/li/div[2]/ul[1]/dl/dd/text()')
    Color = html.xpath('/html/body/section[3]/div/ul/li/div[2]/ul[2]/dl[1]/dd/text()')
    PlayType = html.xpath('/html/body/section[3]/div/ul/li/div[2]/ul[2]/dl[2]/dd/text()')
    PlayInfo = html.xpath('/html/body/section[3]/div/ul/li/div[3]/ul/dl/dd/*/text()')

    return [FilmName, Country, Language, FilmType, OtherFilmName, PlayTime, Color, PlayType, PlayInfo]
