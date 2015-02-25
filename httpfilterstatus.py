#! /usr/bin/env python

import sys
import os
import json
import string
import random




def format_data_http_filter_status(json_http_filter_status,refresh_time):
	bitcount = 8 

	

	try:
		json_npm_traffic_icmp_packets_out = json_http_filter_status["packets_out"] / refresh_time
	except:
		json_npm_traffic_icmp_packets_out = 0











	data = """{
	"agent": {
		"host" : "test.clearclouds.com",
		"pid" : 1234,
		"version" : "1.0.0"
	},
	"components": [
		{
			"name": "jptest",
			"guid": "com.clearclouds.jptest",
			"duration" : 60,
			"metrics" : {
				"Component/Http/Error Rate":%f				
			}
		}
	]
	}""" % (0.05)



	return data