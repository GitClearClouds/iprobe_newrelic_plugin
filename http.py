#! /usr/bin/env python

import sys
import os
import json
import string
import random




def format_data_http(json_http,refresh_time):
	bitcount = 8 	

	try:
		json_http_all = json_http["all"]
	except:
		json_http_all = 0

	try:
		http_latency = json_http_all["LATENCY"]
	except:
		http_latency = 0

	try:
		http_latency_total = json_http_all["LATENCY_TOTAL"]
	except:
		http_latency_total = 0

	try:
		http_bytes= json_http_all["BYTES"] * bitcount / refresh_time
	except:
		http_bytes = 0

	try:
		http_bytes_in = json_http_all["BYTES_IN"] * bitcount / refresh_time
	except:
		http_bytes_in = 0


	try:
		http_bytes_out = json_http_all["BYTES_OUT"] * bitcount / refresh_time
	except:
		http_bytes_out = 0

	try:
		http_requests= json_http_all["REQUESTS"] / refresh_time
	except:
		http_requests = 0











	data = {
		# "Component/Http/Bytes/Total[Bits/Second]": http_bytes,
		"Component/Http/Bytes/In[Bits/Second]": http_bytes_in,
		"Component/Http/Bytes/Out[Bits/Second]": http_bytes_out,
		"Component/Http/Latency/Latency_Total[us]": http_latency_total,
		"Component/Http/Latency/Latency[us]": http_latency,
		"Component/Http/Requests[Count]": http_requests
	}



	# print (http_bytes,http_bytes_in,http_bytes_out,http_latency_total,http_latency,http_requests)


	return data