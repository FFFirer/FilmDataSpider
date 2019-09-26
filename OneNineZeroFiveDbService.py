# -*- coding:utf-8 -*-

import sys
import SqlHelper

# 将数据信息插入数据库
def InsertData(data, FilmId):
    sql = 'INSERT INTO [dbo].[Film1905] ([Name],[Country],[Language],[FilmType],[OtherFilmName],[PlayTime],[Color],[PlayType],[PlayInfo],[FilmId]) \
        VALUES ("%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s" ,"%s", "%s", "%s")'
    
    filmname = data[0]
    country = data[1]
    language = data[2]
    filmtype = data[3]
    othercnfilmname = data[4]
    otherenfilename = data[5]
    playtime = data[6]
    color = data[7]
    playtype = data[8]
    playinfo = data[9]
    userrating = data[10]
    shootingtime = data[11]
    filminglocations = data[12]

    insertsql = '''INSERT INTO [dbo].[Film1905] ([Name],[Country],[Language],[FilmType],[OtherCNFilmName],[OtherENFilmName],[PlayTime],[Color],[PlayType],[PlayInfo],[FilmId],[UserRating],[ShootingTime],[FilmingLocations]) \
        VALUES (%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s, %s, %s, %s, %s)'''

    conn = SqlHelper.Exec(insertsql, (filmname, country, language, filmtype, othercnfilmname, otherenfilename, playtime, color, playtype, playinfo, FilmId, userrating, shootingtime, filminglocations))

# 查询电影Id是否存在
def QueryFilmExists(film_id):
    sql = '''SELECT COUNT(1) FROM Film1905 WHERE FilmId=%s'''
    res = SqlHelper.Query(sql, (film_id))
    if(len(res)>0):
        if(res[0][0]>0):
            return True
    return False