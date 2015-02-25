#! /usr/bin/env python

import sys
import os
import json
import string
import random
import re




def format_data_http_url_status(json_http_url_status,refresh_time):

	pairdata = {}

	for firstkey,firstvalue in json_http_url_status.items() :

		if firstkey != "rate" : continue

		# print(firstvalue) 

		for secondkey,secondvalue in firstvalue.items() :

			if secondkey != "all" : continue

			# print(secondvalue) 


			for thirdvalue in secondvalue :

				if re.match(".*.jpg$",thirdvalue['url']) != None or re.match(".*.php$",thirdvalue['url']) != None : 


					temdata = {}

					strdata = '{"Component/Error rate/%s" : %f}' % (thirdvalue['url'],thirdvalue['rate'] * 100)

					temdata = eval(strdata)

					pairdata.update(temdata) 

	# print(pairdata) 

	return pairdata