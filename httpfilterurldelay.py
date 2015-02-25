#! /usr/bin/env python

import sys
import os
import json
import string
import re


def format_data_http_filter_url_delay(json_http_filter_url_delay,refresh_time):

	pairdata = {}
	
	for firstkey,firstvalue in json_http_filter_url_delay.items() :

		if firstkey != "latency"  : continue

		for secondvalue in firstvalue :

			if re.match(".*.php$",secondvalue['url']) == None : continue


			strdata = '{"Component/Url/Latency/%s" : %d}' % (secondvalue['url'],secondvalue['latency'])

			temdata = eval(strdata)

			pairdata.update(temdata)

	return pairdata