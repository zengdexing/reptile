#!/usr/bin/python
# -*- coding: utf-8 -*-


import urllib2
import urllib
import random
import socket
from bs4 import BeautifulSoup
from time import sleep

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
f = open("2.txt","w")
i = 0
a = 0
while i<1:
	url = 'http://www.mmjpg.com/home/'+str(i)
	socket.setdefaulttimeout(5)
	req = urllib2.Request(url, headers = headers)
	content_stream = urllib2.urlopen(req)
	content_stream = content_stream.read()
	soup = BeautifulSoup(content_stream,'html5lib')
	soupa = soup.select("ul > li > a")
	# soupa = soupa['src']
	print soupa
	for j in soupa:
		# print j['href']
		name = j.select('img')[0]
		# print name['alt']
		url = j['href']
		socket.setdefaulttimeout(5)
		req = urllib2.Request(url, headers = headers)
		try:
			content_stream = urllib2.urlopen(req)
			content_stream = content_stream.read()
			soup = BeautifulSoup(content_stream,'html5lib')
			soup = soup.select('#page > a')
			imgs = soup[-2].get_text()
			print imgs
			lists = 1
			while lists<=int(imgs):
				print lists
				url = j['href']
				socket.setdefaulttimeout(5)
				req = urllib2.Request(url+'/'+str(lists), headers = headers)
				try:
					content_stream = urllib2.urlopen(req)
					content_stream = content_stream.read()
					soup = BeautifulSoup(content_stream,'html5lib')
					soupa = soup.select('#content img')[0]
					print soupa
					lists+=1
					f.write(soupa['src'].encode('utf-8').strip()+'\n')
					path = 'C:\\Users\\xzz64\\Desktop\\python demo\\image\\'+name['alt']+str(lists)+'.jpg'
					urllib.urlretrieve(soupa['src'],path)
					sleep(random.uniform(0.5,1))
				except Exception,e:
					print u'漏掉一张图片' 
					sleep(random.uniform(0.5,1))

		except Exception,e:
			print u'漏掉一个妹子' 
			sleep(random.uniform(0.5,1))

	i+=1
	