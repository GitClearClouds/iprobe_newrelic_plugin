#! /usr/bin/env python

import sys
import os
import json
import string
import random




def format_data_tcp(json_tcp,refresh_time):
	bitcount = 8 



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
		tcp_retransmitted_total_rate = 100 * (json_tcp_all["retransmitted_in"]+json_tcp_all["retransmitted_out"]) / (json_tcp_all["packets_in"]+json_tcp_all["packets_out"]) 
	except:
		tcp_retransmitted_total_rate = 0

	try:
		tcp_retransmitted_in_rate = 100 * json_tcp_all["retransmitted_in"] / json_tcp_all["packets_in"]
	except:
		tcp_retransmitted_in_rate = 0

	try:
		tcp_retransmitted_out_rate = 100 * json_tcp_all["retransmitted_out"] / json_tcp_all["packets_out"]
	except:
		tcp_retransmitted_out_rate = 0




	 
	
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






	data = {
				"Component/Tcp/Latency/Client[us]": tcp_latency_client,
				"Component/Tcp/Latency/Server[us]": tcp_latency_server,		

				"Component/Tcp/AvgPacketLength[Bits]": tcp_packets_avglength,

				# "Component/Tcp/Packet/Total[Packets/Second]": tcp_packets_total,
				"Component/Tcp/Packet/In[Packets/Second]": tcp_packets_in,
				"Component/Tcp/Packet/Out[Packets/Second]": tcp_packets_out,

				# "Component/Tcp/Bytes/Total[Bits/Second]": tcp_bytes_total,
				"Component/Tcp/Bytes/In[Bits/Second]": tcp_bytes_in,
				"Component/Tcp/Bytes/out[Bits/Second]": tcp_bytes_out,

				# "Component/Tcp/Retransmitted/Total[Packets/Second]": tcp_retransmitted_total,
				"Component/Tcp/Retransmitted/In[Packets/Second]": tcp_retransmitted_in,
				"Component/Tcp/Retransmitted/out[Packets/Second]": tcp_retransmitted_out,

				# "Component/Tcp/Retransmitted_rate/Total[%]": tcp_retransmitted_total_rate,
				"Component/Tcp/Retransmitted_rate/In[%]": tcp_retransmitted_in_rate,
				"Component/Tcp/Retransmitted_rate/out[%]": tcp_retransmitted_out_rate,


				# "Component/Tcp/OutOfOrder/Total[Packets/Second]": tcp_ooorder_total,
				"Component/Tcp/OutOfOrder/In[Packets/Second]": tcp_ooorder_in,
				"Component/Tcp/OutOfOrder/out[Packets/Second]": tcp_ooorder_out

			}






	return data