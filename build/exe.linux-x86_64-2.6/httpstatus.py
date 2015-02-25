#! /usr/bin/env python

import sys
import os
import json
import string
import random




def format_data_http_status(json_http_status,refresh_time):
	bitcount = 8 


	try:
		json_http_status_all = json_http_status["all"]
	except:
		json_http_status_all = 0   

	status_code_200_count = 0  
	status_code_2xx_count = 0  
	status_code_3xx_count = 0  
	status_code_4xx_count = 0  
	status_code_5xx_count = 0  


	try:
		for key in json_http_status_all:
			status_code = string.atoi(key)		
			if status_code == 200:
				status_code_200_count += json_http_status_all[key]
			if status_code > 200 and status_code < 300:
				status_code_2xx_count += json_http_status_all[key]
			if status_code >= 300 and status_code < 400:
				status_code_3xx_count += json_http_status_all[key]
			if status_code >= 400 and status_code < 500:
				status_code_4xx_count += json_http_status_all[key]
			if status_code >= 500 and status_code < 600:
				status_code_5xx_count += json_http_status_all[key]
	except:
		status_code_200_count = 0  
		status_code_2xx_count = 0  
		status_code_3xx_count = 0  
		status_code_4xx_count = 0  
		status_code_5xx_count = 0







	data = {
				# "Component/Http/StatusCode/2xx":status_code_2xx_count,
				"Component/Http/StatusCode/3xx":status_code_3xx_count,
				"Component/Http/StatusCode/4xx":status_code_4xx_count,
				"Component/Http/StatusCode/5xx":status_code_5xx_count	
			}

	return data