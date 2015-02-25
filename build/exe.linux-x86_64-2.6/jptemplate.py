#! /usr/bin/env python

import sys
import os
import json
import string
import random




def format_post_connection(json_tcp,json_tcp_connection_all,json_tcp_timeout,json_http,json_http_status,json_npm_traffic,refresh_time):
# def format_post_connection(json_tcp,refresh_time):
	bitcount = 8 
	A1 = random.randrange(0,10000)
	A2 = random.randrange(0,10000)
	A3 = random.randrange(0,10000)
	A4 = random.randrange(0,10000)
	A5 = random.randrange(0,10000)
	A6 = random.randrange(0,10000)

	try:
		tcp_timeout_conns = json_tcp_connection_all["timeout_tcp_conns"] / refresh_time
	except:
		tcp_timeout_conns = 0

	try:
		tcp_reset_conns = json_tcp_connection_all["reset_tcp_conns"] / refresh_time
	except:
		tcp_reset_conns = 0

	try:
		tcp_normal_closed_conns = json_tcp_connection_all["normal_closed_tcp_conns"] / refresh_time
	except:
		tcp_normal_closed_conns = 0

	try:
		tcp_new_conns = json_tcp_connection_all["new_tcp_conns"] / refresh_time
	except:
		tcp_new_conns = 0

	try:
		tcp_closed_conns = json_tcp_connection_all["closed_tcp_conns"] / refresh_time
	except:
		tcp_closed_conns = 0


	try:
		tcp_active_conns = json_tcp_connection_all["active_tcp_conns"] / refresh_time
	except:
		tcp_active_conns = 0


	try:
		tcp_record_counter = json_tcp_connection_all["record_counter"] / refresh_time
	except:
		tcp_record_counter = 0

	try:
		tcp_zero_window = json_tcp_connection_all["zero_window"]
	except:
		tcp_zero_window = 0

	try:
		tcp_syn_pkts_recv = json_tcp_connection_all["syn_pkts_recv"]
	except:
		tcp_syn_pkts_recv = 0


	try:
		json_tcp_all = json_tcp["all"]
	except:
		json_tcp_all = 0

	try:
		tcp_throught = json_tcp_all["bytes_total"] * bitcount / refresh_time
	except:
		tcp_throught = 0

	try:
		tcp_bytes_total = json_tcp_all["bytes_total"] * bitcount / refresh_time
	except:
		tcp_bytes_total = 0

	try:
		tcp_bytes_in = json_tcp_all["bytes_in"] * bitcount / refresh_time
	except:
		tcp_bytes_in = 0

	try:
		tcp_bytes_out = json_tcp_all["bytes_out"] * bitcount / refresh_time
	except:
		tcp_bytes_out = 0

	try:
		tcp_packets_total = json_tcp_all["packets_total"] / refresh_time
	except:
		tcp_packets_total = 0

	try:
		tcp_packets_in = json_tcp_all["packets_in"] / refresh_time
	except:
		tcp_packets_in = 0	

	try:
		tcp_packets_out = json_tcp_all["packets_out"] / refresh_time
	except:
		tcp_packets_out = 0

	try:
		tcp_packets_avglength = json_tcp_all["bytes_total"] / json_tcp_all["packets_total"]
	except:
		tcp_packets_avglength = 0	

	try:
		tcp_ooorder_total = (json_tcp_all["ooorder_in"] + json_tcp_all["ooorder_out"]) / refresh_time
	except:
		tcp_ooorder_total = 0

	try:
		tcp_ooorder_in = json_tcp_all["ooorder_in"] / refresh_time
	except:
		tcp_ooorder_in = 0

	try:
		tcp_ooorder_out = json_tcp_all["ooorder_out"] / refresh_time
	except:
		tcp_ooorder_out = 0



	try:
		tcp_retransmitted_total = (json_tcp_all["retransmitted_in"] + json_tcp_all["retransmitted_out"]) / refresh_time
	except:
		tcp_retransmitted_total = 0

	try:
		tcp_retransmitted_in = json_tcp_all["retransmitted_in"] / refresh_time
	except:
		tcp_retransmitted_in = 0

	try:
		tcp_retransmitted_out = json_tcp_all["retransmitted_out"] / refresh_time
	except:
		tcp_retransmitted_out = 0
	 
	
	try:
		tcp_latency_server = json_tcp_all["server_latency"]
	except:
		tcp_latency_server = 0

	try:
		tcp_latency_client = json_tcp_all["client_latency"]
	except:
		tcp_latency_client = 0

	try:
		tcp_latency_server_total = json_tcp_all["server_latency_total"]
	except:
		tcp_latency_server_total = 0

	try:
		tcp_latency_client_total = json_tcp_all["client_latency_total"]
	except:
		tcp_latency_client_total = 0

	try:
		json_tcp_timeout_all = json_tcp_timeout["all"]
	except:
		json_tcp_timeout_all = 0

	try:
		tcp_scan = json_tcp_timeout_all["scan"]
	except:
		tcp_scan = 0

	try:
		tcp_syn_attacks = json_tcp_timeout_all["syn_attacks"]
	except:
		tcp_syn_attacks = 0


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
				"Component/Tcp/Throught/Active Conn": %d,
				"Component/Tcp/Throught/Traffic": %d,
				"Component/Tcp/Latency/Client": %d,
				"Component/Tcp/Latency/Server": %d,				
				"Component/Tcp/Connection/New": %d,
				"Component/Tcp/Connection/Close": %d,

				"Component/Tcp/Conn/EstaClose/Establish": %d,
				"Component/Tcp/Conn/EstaClose/Close": %d,
				"Component/Tcp/Conn/CloseDetail/Timeout": %d,			
				"Component/Tcp/Conn/CloseDetail/NormalClosed": %d,
				"Component/Tcp/Conn/CloseDetail/Reset": %d,


				"Component/Tcp/Attack/Syn": %d,
				"Component/Tcp/Attack/Scan": %d,				
				"Component/Tcp/CloseState/Fin": %d,
				"Component/Tcp/CloseState/Reset": %d,
				"Component/Tcp/CloseState/Timeout": %d,				
				"Component/Http/Bytes/Totalpackets": %d,
				"Component/Http/Bytes/In": %d,
				"Component/Http/Bytes/Out": %d,
				"Component/Http/Latency/Latency_Total": %d,
				"Component/Http/Latency/Latency": %d,
				"Component/Http/Requests": %d,

				"Component/Tcp/AvgPacketLength": %d,

				"Component/Tcp/Packet/Total": %d,
				"Component/Tcp/Packet/In": %d,
				"Component/Tcp/Packet/Out": %d,

				"Component/Tcp/Bytes/Total": %d,
				"Component/Tcp/Bytes/In": %d,
				"Component/Tcp/Bytes/out": %d,

				"Component/Tcp/Retransmitted/Total": %d,
				"Component/Tcp/Retransmitted/In": %d,
				"Component/Tcp/Retransmitted/out": %d,

				"Component/Tcp/OutOfOrder/Total": %d,
				"Component/Tcp/OutOfOrder/In": %d,
				"Component/Tcp/OutOfOrder/out": %d,

				"Component/UDP/Throught/Total": %d,
				"Component/UDP/Throught/In": %d,
				"Component/UDP/Throught/out": %d,
				"Component/UDP/Packets/Total": %d,
				"Component/UDP/Packets/In": %d,
				"Component/UDP/Packets/out": %d,



				"Component/Npm/Tcp/Packet/Total": %d,
				"Component/Npm/Tcp/Packet/In": %d,
				"Component/Npm/Tcp/Packet/Out": %d,

				"Component/Npm/Tcp/Bytes/Total": %d,
				"Component/Npm/Tcp/Bytes/In": %d,
				"Component/Npm/Tcp/Bytes/out": %d,

				"Component/Npm/Udp/Packet/Total": %d,
				"Component/Npm/Udp/Packet/In": %d,
				"Component/Npm/Udp/Packet/Out": %d,

				"Component/Npm/Udp/Bytes/Total": %d,
				"Component/Npm/Udp/Bytes/In": %d,
				"Component/Npm/Udp/Bytes/out": %d,

				"Component/Npm/Icmp/Packet/Total": %d,
				"Component/Npm/Icmp/Packet/In": %d,
				"Component/Npm/Icmp/Packet/Out": %d,

				"Component/Npm/Icmp/Bytes/Total": %d,
				"Component/Npm/Icmp/Bytes/In": %d,
				"Component/Npm/Icmp/Bytes/out": %d,

				"Component/Npm/Total/Packets": %d,
				"Component/Npm/Total/Bytes": %d,

				"Component/Npm/Tcp/Traffic/Traffic": %d,
				"Component/Npm/Tcp/Traffic/In": %d,
				"Component/Npm/Tcp/Traffic/out": %d,

				
				"Component/Test/Arr":[%d,%d,%d,%d],
				"Component/Test/Num":{
					"min" : 2,
					"max" : 10,
					"total": 12,
					"count" : 2,
					"sum_of_squares" : 104,
					"A" : 34,
					"B" : 56
				},



				"Component/Http/StatusCode/2xx":%d,
				"Component/Http/StatusCode/3xx":%d,
				"Component/Http/StatusCode/4xx":%d,
				"Component/Http/StatusCode/5xx":%d				
			}
		}
	]
	}""" % (tcp_active_conns,json_npm_traffic_tcp_bytes_total,
	tcp_latency_client,tcp_latency_server,tcp_new_conns,tcp_closed_conns,

	tcp_new_conns,tcp_closed_conns,tcp_timeout_conns,tcp_normal_closed_conns,tcp_reset_conns,
	
	tcp_syn_attacks,tcp_scan,tcp_normal_closed_conns,tcp_reset_conns,tcp_timeout_conns,
	http_bytes,http_bytes_in,http_bytes_out,http_latency_total,http_latency,http_requests,
	tcp_packets_avglength,
	tcp_packets_total,tcp_packets_in,tcp_packets_out,
	tcp_bytes_total,tcp_bytes_in,tcp_bytes_out,
	tcp_retransmitted_total,tcp_retransmitted_in,tcp_retransmitted_out,
	tcp_ooorder_total,tcp_ooorder_in,tcp_ooorder_out,
#	udp_bytes_total,udp_bytes_in,udp_bytes_out,udp_packets_total,udp_packets_in,udp_packets_out,
	0,0,0,0,0,0,
	json_npm_traffic_tcp_packets_total,json_npm_traffic_tcp_packets_in,json_npm_traffic_tcp_packets_out,
	json_npm_traffic_tcp_bytes_total,json_npm_traffic_tcp_bytes_in,json_npm_traffic_tcp_bytes_out,
	json_npm_traffic_udp_packets_total,json_npm_traffic_udp_packets_in,json_npm_traffic_udp_packets_out,
	json_npm_traffic_udp_bytes_total,json_npm_traffic_udp_bytes_in,json_npm_traffic_udp_bytes_out,
	json_npm_traffic_icmp_packets_total,json_npm_traffic_icmp_packets_in,json_npm_traffic_icmp_packets_out,
	json_npm_traffic_icmp_bytes_total,json_npm_traffic_icmp_bytes_in,json_npm_traffic_icmp_bytes_out,
	json_npm_traffic_packets_total,json_npm_traffic_bytes_total,

	json_npm_traffic_tcp_bytes_total,json_npm_traffic_tcp_bytes_in,json_npm_traffic_tcp_bytes_out,
	A1,A2,A3,A4,

	status_code_2xx_count,status_code_3xx_count,status_code_4xx_count,status_code_5xx_count)



	print (tcp_active_conns,tcp_throught,tcp_latency_client,tcp_latency_server,tcp_new_conns,tcp_closed_conns,
	tcp_syn_attacks,tcp_scan,tcp_normal_closed_conns,tcp_reset_conns,tcp_timeout_conns,
	http_bytes,http_bytes_in,http_bytes_out,http_latency_total,http_latency,http_requests,
	tcp_packets_avglength,tcp_packets_total,tcp_packets_in,tcp_packets_out,
	tcp_bytes_total,tcp_bytes_in,tcp_bytes_out,
	tcp_retransmitted_total,tcp_retransmitted_in,tcp_retransmitted_out,
	tcp_ooorder_total,tcp_ooorder_in,tcp_ooorder_out,
#	udp_bytes_total,udp_bytes_in,udp_bytes_out,udp_packets_total,udp_packets_in,udp_packets_out,
	0,0,0,0,0,0,
	json_npm_traffic_tcp_packets_total,json_npm_traffic_tcp_packets_in,json_npm_traffic_tcp_packets_out,
	json_npm_traffic_tcp_bytes_total,json_npm_traffic_tcp_bytes_in,json_npm_traffic_tcp_bytes_out,
	json_npm_traffic_udp_packets_total,json_npm_traffic_udp_packets_in,json_npm_traffic_udp_packets_out,
	json_npm_traffic_udp_bytes_total,json_npm_traffic_udp_bytes_in,json_npm_traffic_udp_bytes_out,
	json_npm_traffic_icmp_packets_total,json_npm_traffic_icmp_packets_in,json_npm_traffic_icmp_packets_out,
	json_npm_traffic_icmp_bytes_total,json_npm_traffic_icmp_bytes_in,json_npm_traffic_icmp_bytes_out,
	json_npm_traffic_packets_total,json_npm_traffic_bytes_total,
	A1,A2,A3,A4,

	status_code_200_count,status_code_2xx_count,status_code_3xx_count,status_code_4xx_count,status_code_5xx_count)


	return data