# -*- coding:utf-8 -*-

from lxml import etree



# 获取电影链接
# def GetFilmLink(html_content):
#     html_object = etree.HTML(html_content)
#     target_link = html_object.xpath('//*[@id="filmSearch"]/div[1]/a/@href')
#     return target_link

# 获取电影信息
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

    
    temp = [FilmName, Country, Language, FilmType, OtherFilmName, PlayTime, Color, PlayType, PlayInfo]
    summary = []
    for i in range(len(temp)):
        if(len(temp[i])>0):
            summary.append(','.join(tuple(temp[i])))
            summary[i] = summary[i].replace('\xa0', '')
            if(len(summary[i])>255):
                summary[i] = summary[i][:255]
        else:
            summary.append('') 

    return summary


# 获取下一页链接
def GetNextPageUrl(page_content):
    html = etree.HTML(page_content)
    nextpage_url = html.xpath('//*[@id="new_page"]/a[5]/@href')
    return nextpage_url[0]

# 获取当前页面所有影片的链接
def GetAllFilmeLinkOnPage(page_content):
    html = etree.HTML(page_content)
    film_urls = html.xpath('/html/body/div[2]/div[1]/ul/li/a/@href')

    #print(film_urls)

    return film_urls
