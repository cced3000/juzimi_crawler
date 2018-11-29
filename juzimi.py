#!/usr/bin/python
# -*- coding: utf-8 -*-
# 获取经典句子
import os,sys
import urllib2
import requests
from bs4 import BeautifulSoup

import codecs    #这个模块可以实现。  写入文件编码为 utf-8

reload(sys)
sys.setdefaultencoding('utf-8')
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36',}


baseUrl = 'https://www.juzimi.com/'


content_file = 'content_file.txt'

def get_html(url, i):
    r = requests.get(url, headers = headers)
    html = r.content
    # 写入文件
    # file_name = "juzi" + str(i) + ".html"
    # with codecs.open(file_name, 'a', encoding='utf-8') as f:
    #     f.write(html)
    return html

'''
获取格外的信息
'''

def get_otherInfo(content):
    print "get_otherInfo"
    global content_file
    juzi = content.find('a',class_="xlistju").get_text()   #句子
    love = content.find('a', class_ = "flag-action").get_text()   #喜欢
    comment = content.find('a', class_ = "comment-link").get_text()   # 评论
    user = content.find('a', class_ = "xqusernpop").get_text()   # 用户
    # 写入信息 到 一个表格?/txt
    msg = user + "   " + love + "     " + comment + "    " + juzi + "\n"
    with codecs.open(content_file, 'a', encoding = 'utf-8') as f:
        f.write(msg)
        f.close()

'''
解析html 初步匹配获取大致信息
'''

def get_juzi(html, i):
    soup = BeautifulSoup(html, "lxml")
    allContent = soup.find_all('div',class_ = "views-field-phpcode")
    print '--------------------------------------------'
    print allContent
    for x in allContent:
        get_otherInfo(x)


def get_title(html):
    soup = BeautifulSoup(html, "lxml")
    print soup.title.get_text()

if __name__ == "__main__":
    for item in range(8):
        url = baseUrl + '/article/316132?page=%s' % item
        html = get_html(url, item)
        if item == 0:
            get_title(html)
        get_juzi(html, item)


       