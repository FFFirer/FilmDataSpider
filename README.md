# 目标

抓取时光网上所有的电影

# 技术

* python

## 用到的库

* requests

## 用到的工具

1. sql server 2017 on linux
1. redis

# 抓取网页数据的流程

1. 根据url获取到网页的html
2. 根据指定好的规则获取该网页中的数据
3. 将数据插入到数据库