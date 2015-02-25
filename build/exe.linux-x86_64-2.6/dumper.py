#! /usr/bin/env python

import sys
import os
import time
import json
import string
import datetime
import random
import re
import commands



istest = False




def get_url(ip,user):

	if istest : 

		proto = "sftp"

		loginname = user + "@" + ip

		url = proto + "://" + loginname

	else :

		url = ''

	return url



def get_http_file(tm,refresh_time):

	if istest : 
		folder = tm.strftime("/public/nfcapd-file/live/peer1/http/%Y/%m/%d/%H/")
	else :
		folder = tm.strftime("/home/juyun/datafile/nfcapd-file/live/peer1/http/%Y/%m/%d/%H/")

	# filename = tm.strftime("nfcapd_http.%Y%m%d%H%M00")


	q,r = divmod(tm.second,refresh_time)
	i = q * refresh_time
	if i == 60 : i = 0

	filename = tm.strftime("nfcapd_http.%Y%m%d%H%M") + "%0.2d" % i



	path = folder + filename


	# path = '/root/workspace/juyundata/nfcap/nfcapd_http.20150129160000'

	return path


def get_tcp_file(tm,refresh_time):

	if istest : 
		folder = tm.strftime("/public/nfcapd-file/live/peer1/tcp/%Y/%m/%d/%H/")
	else :
		folder = tm.strftime("/home/juyun/datafile/nfcapd-file/live/peer1/tcp/%Y/%m/%d/%H/")
		
	# filename = tm.strftime("nfcapd_tcp.%Y%m%d%H%M00")


	q,r = divmod(tm.second,refresh_time)
	i = q * refresh_time
	if i == 60 : i = 0

	filename = tm.strftime("nfcapd_tcp.%Y%m%d%H%M") + "%0.2d" % i


	path = folder + filename

	return path



def analyze_tcp_file(tm,refresh_time):

	url = get_url('192.168.10.67','root')

	filename = url + get_tcp_file(tm,refresh_time)

	dumpcmd = 'nfdump -r ' + filename

	dumparg = ' -p 1 -A distip/srcip '

	fmt = ' -o "fmt:%url%appl_latency_ave%appl_latency_min%appl_latency_max"'


	dumpcommand = dumpcmd + dumparg + fmt


	rslt = os.popen(dumpcommand).readlines() 


	return rslt



def analyze_http_file(tm,refresh_time):

	url = get_url('192.168.10.67','root')

	filename = url + get_http_file(tm,refresh_time)

	dumpcmd = 'nfdump -r ' + filename

	dumparg = ' -p 2 -A host/url '

	fmt = ' -o "fmt:%url%appl_latency_ave%appl_latency_min%appl_latency_max"'

	dumpcommand = dumpcmd + dumparg + fmt

	print(dumpcmd)

	rslt = os.popen(dumpcommand).readlines() 


	for item in rslt :
		item2 = item.split()
		for item3 in item2 :
			print(item3)
		print('-----------------------------------------------------------------------------------------')

	result = rslt[1:]


	return result




def get_http_data(tm,refresh_time):

	url = get_url('192.168.10.67','root')

	filename = url + get_http_file(tm,refresh_time)

	dumpcmd = 'nfdump -r ' + filename

	dumparg = ' -p 2 -A host/url '

	fmt = ' -o "fmt:%url%appl_latency_ave%appl_latency_min%appl_latency_max"'

	dumparg = ''

	fmt = ''

	dumpcommand = dumpcmd + dumparg + fmt

	print(dumpcommand)

	rslt = os.popen(dumpcommand).readlines() 

	result = rslt[1:]


	return result


# tm = datetime.datetime.now()
# tm = tm - datetime.timedelta(minutes = 1)

# rslt = analyze_http_file(tm)

# print(rslt)




# output = os.system("ls")

# status , output = commands.getstatusoutput('ls -l')


# output = os.popen("ll",'r')

# print(output)


# print os.popen('ls -lt').readlines() 

# print os.popen('ls -lt').read() 

