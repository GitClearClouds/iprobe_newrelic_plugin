#! /usr/bin/env python

import sys
import os
import json
import string
import random
import re




def format_data_http_url(json_http_url,refresh_time):

	print('format_data_http_url') 

	pairdata = {}

	for firstkey,firstvalue in json_http_url.items() :

		if firstkey != "latency" : continue

		print('firstvalue',firstvalue) 

		for secondkey,secondvalue in firstvalue.items() :

			if secondkey != "all" : continue

			print('secondvalue',secondvalue) 


			for thirdvalue in secondvalue :

				print('thirdvalue',thirdvalue) 

				if re.match(".*.jpg$",thirdvalue['url']) == None and re.match(".*.php$",thirdvalue['url']) == None : continue

				temdata = {}

				strdata = '{"Component/Url/Latency/%s" : %d}' % (thirdvalue['url'],thirdvalue['latency'])

				temdata = eval(strdata)

				pairdata.update(temdata) 

	# print(pairdata) 

	return pairdata