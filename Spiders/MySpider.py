# -*- coding:utf-8 -*-

import requests

Headers1 = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Language': 'zh,zh-TW;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6',
            'Connection': 'keep-alive'}

# 返回utf8编码的html
def GetHtml(url):
    origin_html = requests.get(url)
    return origin_html.text

# 1905网的Header
def GetHtmlWithHeader(url):
    origin_html = requests.get(url, headers=Headers1)
    return origin_html.text