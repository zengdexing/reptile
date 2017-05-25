#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2
import random
import socket
from bs4 import BeautifulSoup
from time import sleep


user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'   
headers = { 'User-Agent' : user_agent }  
mark = 0
f = open('douban.txt','w')
while mark<10:

	Subscript = mark * 25
	req = urllib2.Request('https://movie.douban.com/top250?start='+str(Subscript), headers = headers)  
	socket.setdefaulttimeout(5)
	try:
		req = urllib2.urlopen(req).read()
		lista = BeautifulSoup(req, "html5lib")
		soup = lista.select(".grid_view .info")


	

		for i in soup:
			soupa = i.select(".hd a span")
			soupb = i.select(".bd p")[0]
			stra = ''
			for j in soupa:
				# print j.get_text(',', strip=True).encode('utf8')
				stra += j.get_text(',', strip=True).encode('utf8')


			f.write(stra+'\n')	
			# print soupb.get_text(',', strip=True).encode('utf8')
			f.write(soupb.get_text(',', strip=True).encode('utf8')+'\n')
			soupc = i.select(".star span")[1]
			# print soupc.get_text(',', strip=True)
			f.write(soupc.get_text(',', strip=True).encode('utf8')+'\n')
			soupc = i.select(".star span")[3]
			# print soupc.get_text(',', strip=True).encode('utf8')
			f.write(soupc.get_text(',', strip=True).encode('utf8')+'\n')
			if i.select(".quote span"):
				soupd = i.select(".quote span")[0]
				f.write(soupd.get_text(',', strip=True).encode('utf8')+'\n')



		mark = mark+1
		sleep(random.uniform(1,5))
	except Exception,e:
		print str(Subscript)+u'页抓取失败'
		sleep(random.uniform(0.5,1))
	# f = open('xiao.txt','w')
	# for i in range(len(soup)):
	# 	# print i.get_text().encode('utf8')
	# 	f.write(soup[i].get_text().encode('utf8'))
	# 	# f.write(soupa[i].get_text().encode('utf8'))
	# # print soup

