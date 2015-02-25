#! /usr/bin/env python

import sys
import os
import json
import string
import random
import re




def format_data_http_filter_url_status(json_http_filter_url_status,refresh_time):

	pairdata = {}
	
	for firstkey,firstvalue in json_http_filter_url_status.items() :

		if firstkey != "rate" : continue

		for secondvalue in firstvalue :

			if re.match(".*.jpg$",secondvalue['url']) != None or re.match(".*.php$",secondvalue['url']) != None : 
				

				temdata = {}

				strdata = '{"Component/Error rate/%s" : %f}' % (secondvalue['url'],secondvalue['rate'])

				temdata = eval(strdata)

				pairdata.update(temdata) 

	return pairdata


def format_data_http_filter_url_status2(json_http_filter_url_status,refresh_time):

	pairdata = {}
	
	for firstkey,firstvalue in json_http_filter_url_status.items() :

		if firstkey != "rate"  and  firstkey != "error"  : continue

		for secondvalue in firstvalue :

			if re.match(".*.jpg$",secondvalue['url']) != None or re.match(".*.php$",secondvalue['url']) != None : 
				
				print(secondvalue['url'],"is ok") 


				# pairdata = """{"%s":%f}""" % (secondvalue['url'],secondvalue['rate'])	

				# print(temdata) 

				temdata = {}

				strdata = '{"Component/Error rate/%s" : %f}' % (secondvalue['url'],secondvalue['rate'] * 100)

				temdata = eval(strdata)

				# temdata["Component/Test/Url/"+secondvalue['url']] = secondvalue['rate']


				pairdata.update(temdata) 

	return pairdata