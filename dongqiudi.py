#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# Copyright [c] 2016 By Ansion All rights Reserved.
import requests
import time
import re
from bs4 import BeautifulSoup as bfs

import mysql.connector as connector

#采集懂球帝头条文章
#存进mysql数据库
#使用linux中的crontab每天定时执行

#获得列表前n篇文章id
def get_list():
    url = 'http://m.dongqiudi.com/api/mobile/tab/1/archives'
    list = requests.get(url)
    return list.json()['list']['articles']

#查找数据库文章aid是否已经存在，不存在返回None
def check_id(aid):
    cur.execute("select sort from article where sort="+(aid))
    return cur.fetchone()

#下载文章封面图片
# def download_pic(url):
#     pass

#根据id获取文章内容
def get_content(url):
    content = requests.get(url).text
    soup = bfs(content, 'html.parser')
    title = soup.title.string
    author = soup.writer
    if (author == None):
        author = ''
    else:
        author = author.string
    time_1 = time.mktime(time.strptime(soup.time.string, '%Y-%m-%d %H:%M:%S'))
    content = soup.find('div', {'class':'con'})
    photo = soup.article.img
    if(photo == None):
        photo = ''
    else:
        photo = photo.get('src')
    data = [str(title), str(title), str(author), float(time_1), str(content), photo,2]
    return data

#正则截取文章aid
def get_aid(x):
    return str(re.search(r'[0-9]{6,8}', str(x)).group())

#正常情况能获取前五篇文章
if __name__ == '__main__':

    # 连接数据库
    config = {
        'user': '',
        'password': '',
        'host': '',
        'port': 3306,
        'database': ''
    }
    conn = connector.connect(**config)
    cur = conn.cursor(buffered=True)

    artlist = r'http://www.dongqiudi.com/share/article/'
    url_list = []

    #循环获取5篇文章的aid
    for x in get_list()[:5]:
        url_list.append(artlist+str(x['aid']))

    #循环check_id文章是否已经存在数据库，没有并且文章中有图片则插入数据库
    for x in url_list:
        data = get_content(x)
        aid = get_aid(x)
        if(check_id(aid)==None):
            data.append(int(aid))
            if(data[5] != ''):
                print("文章保存成功", data[0])
                cur.execute("INSERT into article (title, summary, author, time, "
                            "content, photo_path, nav, sort) values"
                            " (%s,%s,%s,%s,%s,%s,%s, %s)", data)
            else:
                continue
        else:
            print("文章已存在", data[0])
    
    cur.close()
    conn.close()

#关闭数据库连接
