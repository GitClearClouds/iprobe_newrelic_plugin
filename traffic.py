#! /usr/bin/env python

import sys
import os
import json
import string
import random




def format_data_npm_traffic(json_npm_traffic,refresh_time):
	bitcount = 8 

	
	try:
		json_npm_traffic_tcp = json_npm_traffic["TCP"]
	except:
		json_npm_traffic_tcp = 0  

	try:
		json_npm_traffic_tcp_bytes_total = json_npm_traffic_tcp["bytes_total"] * bitcount / refresh_time
	except:
		json_npm_traffic_tcp_bytes_total = 0

	try:
		json_npm_traffic_tcp_bytes_in = json_npm_traffic_tcp["bytes_in"] * bitcount / refresh_time
	except:
		json_npm_traffic_tcp_bytes_in = 0

	try:
		json_npm_traffic_tcp_bytes_out = json_npm_traffic_tcp["bytes_out"] * bitcount / refresh_time
	except:
		json_npm_traffic_tcp_bytes_out = 0

	try:
		json_npm_traffic_tcp_packets_total = json_npm_traffic_tcp["packets_total"] / refresh_time
	except:
		json_npm_traffic_tcp_packets_total = 0

	try:
		json_npm_traffic_tcp_packets_in = json_npm_traffic_tcp["packets_in"] / refresh_time
	except:
		json_npm_traffic_tcp_packets_in = 0

	try:
		json_npm_traffic_tcp_packets_out = json_npm_traffic_tcp["packets_out"] / refresh_time
	except:
		json_npm_traffic_tcp_packets_out = 0




	try:
		json_npm_traffic_udp = json_npm_traffic["UDP"]
	except:
		json_npm_traffic_udp = 0  

	try:
		json_npm_traffic_udp_bytes_total = json_npm_traffic_udp["bytes_total"] * bitcount / refresh_time
	except:
		json_npm_traffic_udp_bytes_total = 0

	try:
		json_npm_traffic_udp_bytes_in = json_npm_traffic_udp["bytes_in"] * bitcount / refresh_time
	except:
		json_npm_traffic_udp_bytes_in = 0

	try:
		json_npm_traffic_udp_bytes_out = json_npm_traffic_udp["bytes_out"] * bitcount / refresh_time
	except:
		json_npm_traffic_udp_bytes_out = 0

	try:
		json_npm_traffic_udp_packets_total = json_npm_traffic_udp["packets_total"] / refresh_time
	except:
		json_npm_traffic_udp_packets_total = 0

	try:
		json_npm_traffic_udp_packets_in = json_npm_traffic_udp["packets_in"] / refresh_time
	except:
		json_npm_traffic_udp_packets_in = 0

	try:
		json_npm_traffic_udp_packets_out = json_npm_traffic_udp["packets_out"] / refresh_time
	except:
		json_npm_traffic_udp_packets_out = 0





	try:
		json_npm_traffic_icmp = json_npm_traffic["ICMP"]
	except:
		json_npm_traffic_icmp = 0  

	try:
		json_npm_traffic_icmp_bytes_total = json_npm_traffic_icmp["bytes_total"] * bitcount / refresh_time
	except:
		json_npm_traffic_icmp_bytes_total = 0

	try:
		json_npm_traffic_icmp_bytes_in = json_npm_traffic_icmp["bytes_in"] * bitcount / refresh_time
	except:
		json_npm_traffic_icmp_bytes_in = 0

	try:
		json_npm_traffic_icmp_bytes_out = json_npm_traffic_icmp["bytes_out"] * bitcount / refresh_time
	except:
		json_npm_traffic_icmp_bytes_out = 0

	try:
		json_npm_traffic_icmp_packets_total = json_npm_traffic_icmp["packets_total"] / refresh_time
	except:
		json_npm_traffic_icmp_packets_total = 0

	try:
		json_npm_traffic_icmp_packets_in = json_npm_traffic_icmp["packets_in"] / refresh_time
	except:
		json_npm_traffic_icmp_packets_in = 0

	try:
		json_npm_traffic_icmp_packets_out = json_npm_traffic_icmp["packets_out"] / refresh_time
	except:
		json_npm_traffic_icmp_packets_out = 0


	json_npm_traffic_bytes_total = json_npm_traffic_tcp_bytes_total + json_npm_traffic_udp_bytes_total + json_npm_traffic_icmp_bytes_total
	json_npm_traffic_packets_total = json_npm_traffic_tcp_packets_total + json_npm_traffic_udp_packets_total + json_npm_traffic_icmp_packets_total











	# data = """{
	# "agent": {
	# 	"host" : "test.clearclouds.com",
	# 	"pid" : 1234,
	# 	"version" : "1.0.0"
	# },
	# "components": [
	# 	{
	# 		"name": "jptest",
	# 		"guid": "com.clearclouds.jptest",
	# 		"duration" : 60,
	# 		"metrics" : {
	# 			"Component/Npm/Tcp/Packet/Total": %d,
	# 			"Component/Npm/Tcp/Packet/In": %d,
	# 			"Component/Npm/Tcp/Packet/Out": %d,

	# 			"Component/Npm/Tcp/Bytes/Total": %d,
	# 			"Component/Npm/Tcp/Bytes/In": %d,
	# 			"Component/Npm/Tcp/Bytes/out": %d,

	# 			"Component/Npm/Udp/Packet/Total": %d,
	# 			"Component/Npm/Udp/Packet/In": %d,
	# 			"Component/Npm/Udp/Packet/Out": %d,

	# 			"Component/Npm/Udp/Bytes/Total": %d,
	# 			"Component/Npm/Udp/Bytes/In": %d,
	# 			"Component/Npm/Udp/Bytes/out": %d,

	# 			"Component/Npm/Icmp/Packet/Total": %d,
	# 			"Component/Npm/Icmp/Packet/In": %d,
	# 			"Component/Npm/Icmp/Packet/Out": %d,

	# 			"Component/Npm/Icmp/Bytes/Total": %d,
	# 			"Component/Npm/Icmp/Bytes/In": %d,
	# 			"Component/Npm/Icmp/Bytes/out": %d,

	# 			"Component/Npm/Total/Packets": %d,
	# 			"Component/Npm/Total/Bytes": %d,

	# 			"Component/Npm/Tcp/Traffic/Traffic": %d,
	# 			"Component/Npm/Tcp/Traffic/In": %d,
	# 			"Component/Npm/Tcp/Traffic/out": %d
	# 		}
	# 	}
	# ]
	# }""" % (
	# 		json_npm_traffic_tcp_packets_total,
	# 		json_npm_traffic_tcp_packets_in,
	# 		json_npm_traffic_tcp_packets_out,

	# 		json_npm_traffic_tcp_bytes_total,
	# 		json_npm_traffic_tcp_bytes_in,
	# 		json_npm_traffic_tcp_bytes_out,

	# 		json_npm_traffic_udp_packets_total,
	# 		json_npm_traffic_udp_packets_in,
	# 		json_npm_traffic_udp_packets_out,

	# 		json_npm_traffic_udp_bytes_total,
	# 		json_npm_traffic_udp_bytes_in,
	# 		json_npm_traffic_udp_bytes_out,

	# 		json_npm_traffic_icmp_packets_total,
	# 		json_npm_traffic_icmp_packets_in,
	# 		json_npm_traffic_icmp_packets_out,

	# 		json_npm_traffic_icmp_bytes_total,
	# 		json_npm_traffic_icmp_bytes_in,
	# 		json_npm_traffic_icmp_bytes_out,

	# 		json_npm_traffic_packets_total,
	# 		json_npm_traffic_bytes_total,
			
	# 		json_npm_traffic_tcp_bytes_total,
	# 		json_npm_traffic_tcp_bytes_in,
	# 		json_npm_traffic_tcp_bytes_out)


	data = {
				# "Component/Npm/Tcp/Packet/Total[Packets/Second]": json_npm_traffic_tcp_packets_total,
				"Component/Npm/Tcp/Packet/In[Packets/Second]": json_npm_traffic_tcp_packets_in,
				"Component/Npm/Tcp/Packet/Out[Packets/Second]": json_npm_traffic_tcp_packets_out,

				# "Component/Npm/Tcp/Bytes/Total[Bits/Second]": json_npm_traffic_tcp_bytes_total,
				"Component/Npm/Tcp/Bytes/In[Bits/Second]": json_npm_traffic_tcp_bytes_in,
				"Component/Npm/Tcp/Bytes/out[Bits/Second]": json_npm_traffic_tcp_bytes_out,

				# "Component/Npm/Udp/Packet/Total[Packets/Second]": json_npm_traffic_udp_packets_total,
				"Component/Npm/Udp/Packet/In[Packets/Second]": json_npm_traffic_udp_packets_in,
				"Component/Npm/Udp/Packet/Out[Packets/Second]": json_npm_traffic_udp_packets_out,

				# "Component/Npm/Udp/Bytes/Total[Bits/Second]": json_npm_traffic_udp_bytes_total,
				"Component/Npm/Udp/Bytes/In[Bits/Second]": json_npm_traffic_udp_bytes_in,
				"Component/Npm/Udp/Bytes/out[Bits/Second]": json_npm_traffic_udp_bytes_out,

				# "Component/Npm/Icmp/Packet/Total[Packets/Second]": json_npm_traffic_icmp_packets_total,
				"Component/Npm/Icmp/Packet/In[Packets/Second]": json_npm_traffic_icmp_packets_in,
				"Component/Npm/Icmp/Packet/Out[Packets/Second]": json_npm_traffic_icmp_packets_out,

				# "Component/Npm/Icmp/Bytes/Total[Bits/Second]": json_npm_traffic_icmp_bytes_total,
				"Component/Npm/Icmp/Bytes/In[Bits/Second]": json_npm_traffic_icmp_bytes_in,
				"Component/Npm/Icmp/Bytes/out[Bits/Second]": json_npm_traffic_icmp_bytes_out,

				"Component/Npm/Total/Packets[Packets/Second]": json_npm_traffic_packets_total,
				"Component/Npm/Total/Bytes[Bits/Second]": json_npm_traffic_bytes_total,

				"Component/Npm/Tcp/Traffic/Traffic[Bits/Second]": json_npm_traffic_tcp_bytes_total,
				"Component/Npm/Tcp/Traffic/In[Bits/Second]": json_npm_traffic_tcp_bytes_in,
				"Component/Npm/Tcp/Traffic/out[Bits/Second]": json_npm_traffic_tcp_bytes_out
			}



	return data