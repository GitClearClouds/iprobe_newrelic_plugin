#! /usr/bin/env python

import sys
import os
import json
import string
import random




def format_data_tcp_timeout(json_tcp_timeout,refresh_time):

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


	data = {}

	temdata = {}

	strdata = '{"Component/Tcp/Attack/Syn[Count/Second]" : %d}' % (tcp_syn_attacks)

	temdata = eval(strdata)

	data.update(temdata) 

	strdata = '{"Component/Tcp/Attack/Scan[Count/Second]" : %d}' % (tcp_scan)

	temdata = eval(strdata)

	data.update(temdata) 





	# data = {
	# 			"Component/Tcp/Attack/Syn": tcp_syn_attacks,
	# 			"Component/Tcp/Attack/Scan": tcp_scan
	# 		}


	return data