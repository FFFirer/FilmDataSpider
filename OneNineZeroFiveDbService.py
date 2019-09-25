# -*- coding:utf-8 -*-

import sys
import SqlHelper

# 将数据信息插入数据库
def InsertData(data, FilmId):
    sql = 'INSERT INTO [dbo].[Film1905] ([Name],[Country],[Language],[FilmType],[OtherFilmName],[PlayTime],[Color],[PlayType],[PlayInfo],[FilmId]) \
        VALUES ("%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s")'
    
    filmname = data[0]
    country = data[1]
    language = data[2]
    filmtype = data[3]
    otherfilmname = data[4]
    playtime = data[5]
    color = data[6]
    playtype = data[7]
    playinfo = data[8]

    insertsql = '''INSERT INTO [dbo].[Film1905] ([Name],[Country],[Language],[FilmType],[OtherFilmName],[PlayTime],[Color],[PlayType],[PlayInfo],[FilmId]) \
        VALUES (%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s)'''

    conn = SqlHelper.Exec(insertsql, (filmname, country, language, filmtype, otherfilmname, playtime, color, playtype, playinfo, FilmId))

# 查询电影Id是否存在
def QueryFilmExists(film_id):
    sql = '''SELECT COUNT(1) FROM Film1905 WHERE FilmId=%s'''
    res = SqlHelper.Query(sql, (film_id))
    if(len(res)>0):
        if(res[0][0]>0):
            return True
    return False