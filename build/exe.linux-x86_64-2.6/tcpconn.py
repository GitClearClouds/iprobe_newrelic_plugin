#! /usr/bin/env python

import sys
import os
import time
import json
import string
import datetime
import random



def format_data_tcp_connection(json_tcp_connection_all,refresh_time):
	bitcount = 8 

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
	# 			"Component/Tcp/Throught/Active Conn" : %d,
	# 			"Component/Tcp/Connection/New" : %d,
	# 			"Component/Tcp/Connection/Close" : %d,

	# 			"Component/Tcp/Conn/EstaClose/Establish" : %d,
	# 			"Component/Tcp/Conn/EstaClose/Close" : %d,
	# 			"Component/Tcp/Conn/CloseDetail/Timeout" : %d,
	# 			"Component/Tcp/Conn/CloseDetail/NormalClosed" : %d,
	# 			"Component/Tcp/Conn/CloseDetail/Reset" : %d,

	# 			"Component/Tcp/CloseState/Fin" : %d,
	# 			"Component/Tcp/CloseState/Reset" : %d,
	# 			"Component/Tcp/CloseState/Timeout" : %d
	# 		}
	# 	}
	# ]
	# }""" % (tcp_active_conns,
	# 		tcp_new_conns,
	# 		tcp_closed_conns,
	# 		tcp_new_conns,
	# 		tcp_closed_conns,
	# 		tcp_timeout_conns,
	# 		tcp_normal_closed_conns,
	# 		tcp_reset_conns,	
	# 		tcp_normal_closed_conns,
	# 		tcp_reset_conns,
	# 		tcp_timeout_conns)

	data = {
				"Component/Tcp/Throught/Active Conn[Count/Second]" : tcp_active_conns,
				"Component/Tcp/Connection/New[Count/Second]" : tcp_new_conns,
				"Component/Tcp/Connection/Close[Count/Second]" : tcp_closed_conns,

				"Component/Tcp/Conn/EstaClose/Establish[Count/Second]" : tcp_new_conns,
				"Component/Tcp/Conn/EstaClose/Close[Count/Second]" : tcp_closed_conns,
				"Component/Tcp/Conn/CloseDetail/Timeout[Count/Second]" : tcp_timeout_conns,
				"Component/Tcp/Conn/CloseDetail/NormalClosed[Count/Second]" : tcp_normal_closed_conns,
				"Component/Tcp/Conn/CloseDetail/Reset[Count/Second]" : tcp_reset_conns,

				"Component/Tcp/CloseState/Fin[Count/Second]" : tcp_normal_closed_conns,
				"Component/Tcp/CloseState/Reset[Count/Second]" : tcp_reset_conns,
				"Component/Tcp/CloseState/Timeout[Count/Second]" : tcp_timeout_conns
			}





	return data