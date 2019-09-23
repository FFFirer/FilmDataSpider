# -*- coding:utf-8 -*-

import sys
sys.path.append('E:\CodeRepos\FilmDataSpider')
import SqlHelper

# 将数据信息插入数据库
def HandleData(data, FilmId):
    sql = 'INSERT INTO [dbo].[Film1905] ([Name],[Country],[Language],[FilmType],[OtherFilmName],[PlayTime],[Color],[PlayType],[PlayInfo],[FilmId]) \
        VALUES ("%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s")'
    
    filmname = ','.join(data[0])
    country = ','.join(data[1])
    language = ','.join(data[2])
    filmtype = ','.join(data[3])
    otherfilmname = ','.join(data[4])
    playtime = ','.join(data[5])
    color = ','.join(data[6])
    playtype = ','.join(data[7])
    playinfo = ','.join(data[8])

    insertsql = str.format('INSERT INTO [dbo].[Film1905] ([Name],[Country],[Language],[FilmType],[OtherFilmName],[PlayTime],[Color],[PlayType],[PlayInfo],[FilmId]) \
        VALUES ("%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s")' % (filmname, country, language, filmtype, otherfilmname, playtime, color, playtype, playinfo, FilmId))

    conn = SqlHelper.Exec(insertsql)