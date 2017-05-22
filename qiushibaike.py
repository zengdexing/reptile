#!/usr/bin/python
# -*- coding: utf-8 -*-


import urllib2
from bs4 import BeautifulSoup


user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'   
headers = { 'User-Agent' : user_agent }  
req = urllib2.Request('http://www.qiushibaike.com/', headers = headers)  
content_stream = urllib2.urlopen(req)
content_stream = content_stream.read()
soup = BeautifulSoup(content_stream,'html5lib')
soupa = soup.select(".content")
soupb = soup.select(".stats-vote")
f = open("xiao.txt","w")
for index in range(len(soupa)):
    print soupa[index].get_text("|", strip=True)
    print soupb[index].get_text("|", strip=True)
    f.write(soupa[index].get_text("|", strip=True).encode('utf-8').strip()+'\n')
    f.write(soupb[index].get_text("|", strip=True).encode('utf-8').strip()+'\n')
    f.write('\n\n')


# print soupa[20].get_text()
# print len(soupb)
# print len(soupa)