#! /usr/bin/env python

import sys
import os
import urllib2
import time
import json
import string
import datetime
import random
import ConfigParser
import tcp
import tcpconn
import tcptimeout
import http
import httpstatus
import httpfilterstatus
import httpfilterurlstatus
import traffic
import jptemplate
import apdex
import httpfilterurldelay
import httpurlstatus
import httpurl
import errorrate
import httplatency
import dumper
import getopt
import common





testing = False


datadir = '/home/juyun/datafile'
newrelickey = '19e4cb7a2ec9c43a7a90cec3360fb7b5868d08d6'
pluginname = 'ClearClouds'
juyuninidir = '/usr/local/etc'
juyunini_newrelic = juyuninidir + '/newrelic.ini'







def get_commandline() :

	global datadir 
	global newrelickey 
	global pluginname 
	global juyunini_newrelic 

	try :

		config = ConfigParser.ConfigParser()
		config.read(juyunini_newrelic)


		datadir = config.get("newrelic","datadir")
		newrelickey = config.get("newrelic","newrelickey")
		pluginname = config.get("newrelic","pluginname")

	except : 

		datadir = '/home/juyun/datafile'
		newrelickey = '19e4cb7a2ec9c43a7a90cec3360fb7b5868d08d6'
		pluginname = 'Clearclouds'


	# print(datadir)
	# print(newrelickey)
	# print(pluginname)

	return pluginname


# def read_newrelic_key():

# 	global juyunini_newrelic 

# 	try:
# 		config = ConfigParser.ConfigParser()
# 		config.read(juyunini_newrelic)
# 		newrelickey = config.get("newrelic","newrelickey")

# 		return newrelickey
# 	except : pass

# 	return newrelickey



def usage():  
	print("Usage:%s [-d|-k|-n|-h] [--help] args...." % sys.argv[0]);  
	print("-r run execute fetcher ");  
	print("-d data directory");  
	print("-k new relic license key");  
	print("-n plugin name ");  




def analyse_commandline(refresh_time) :


	try :
		opts,args = getopt.getopt(sys.argv[1:], "rthd:k:n:", ["help"])


		if opts == [] :

			usage()
			sys.exit(1);  


		for opt,arg in opts:  

			if opt in ("-h", "--help"):

				usage()
				sys.exit(1);  

			elif opt in ("-d") :

				dodir(arg) 

			elif opt in ("-k") :

				dokey(arg)


			elif opt in ("-n") :

				doname(arg)

			elif opt in ("-t") :

				common.setistest(True)

		for opt,arg in opts:  

			if opt in ("-r") :

				doprintini()

				ExcuteFetcher(refresh_time)			

		doprintini()


	except getopt.GetoptError:

		print("getopt error!")
		usage()
		# sys.exit(1);








def dokey(key) :

	global juyuninidir 
	global juyunini_newrelic 

	try :

		if not os.path.exists(juyuninidir) :

			dumpcommand = 'mkdir -p '+ juyuninidir

			os.popen(dumpcommand)


		if not os.path.exists(juyunini_newrelic) :

			f = open(juyunini_newrelic,'a+')
			f.write('[newrelic]')
			f.write('datadir = ')
			f.write('newrelickey = ')
			f.write('pluginname = ')
			f.write(sys.argv[1])
			f.close()


		config = ConfigParser.ConfigParser()
		config.read(juyunini_newrelic)
		config.set("newrelic","newrelickey",key)
		config.write(open(juyunini_newrelic,'w'))

		# doprintini()


	except : pass


def dodir(key) :

	global juyuninidir 
	global juyunini_newrelic 

	try :

		if not os.path.exists(juyuninidir) :

			dumpcommand = 'mkdir -p '+ juyuninidir

			os.popen(dumpcommand)


		if not os.path.exists(juyunini_newrelic) :

			f = open(juyunini_newrelic,'a+')
			f.write('[newrelic]')
			f.write('datadir = ')
			f.write('newrelickey = ')
			f.write('pluginname = ')
			f.write(sys.argv[1])
			f.close()


		config = ConfigParser.ConfigParser()
		config.read(juyunini_newrelic)
		config.set("newrelic","datadir",key)
		config.write(open(juyunini_newrelic,'w'))

		# doprintini()


	except : pass


def doname(key) :

	global juyuninidir 
	global juyunini_newrelic  

	try :

		if not os.path.exists(juyuninidir) :

			dumpcommand = 'mkdir -p '+ juyuninidir

			os.popen(dumpcommand)


		if not os.path.exists(juyunini_newrelic) :

			f = open(juyunini_newrelic,'a+')
			f.write('[newrelic]')
			f.write('datadir = ')
			f.write('newrelickey = ')
			f.write('pluginname = ')
			f.write(sys.argv[1])
			f.close()


		config = ConfigParser.ConfigParser()
		config.read(juyunini_newrelic)
		config.set("newrelic","pluginname",key)
		config.write(open(juyunini_newrelic,'w'))

		# doprintini()


	except : pass





def doprintini() :

	global juyuninidir 
	global juyunini_newrelic 

	try :

		config = ConfigParser.ConfigParser()

		config.read(juyunini_newrelic)

		vvv =  "datadir = " + config.get("newrelic","datadir")
		print(vvv)

		vvv =  "newrelickey = " + config.get("newrelic","newrelickey")
		print(vvv)

		vvv =  "pluginname = " + config.get("newrelic","pluginname")
		print(vvv)


	except : pass







# def post_data(url, data):

# 	global newrelickey

# 	try:
# 		request = urllib2.Request(url, data, {'X-License-Key': newrelickey, 'Content-Type': 'application/json', 'Accept': 'application/json'})
# 		response = urllib2.urlopen(request)
# 		if response.getcode() != 200:
# 			print 'post status code:', response.getcode()
# 		else:
# 			print response.read()
# 	except Exception, e:
# 		print 'post exception:', str(e)



def post_newrelic(data):

	result = False

	global newrelickey
	url = 'https://platform-api.newrelic.com/platform/v1/metrics'

	try:
		request = urllib2.Request(url, data, {'X-License-Key': newrelickey, 'Content-Type': 'application/json', 'Accept': 'application/json'})
		response = urllib2.urlopen(request)
		if response.getcode() != 200:
			print 'post status code:', response.getcode()
			result = False
		else:
			print response.read()
			result = True

	except Exception, e:
		print 'post exception:', str(e)


	return result





def get_refresh_time():
	try:
		config = ConfigParser.ConfigParser()
		config.read("/usr/local/etc/nfsen.ini")
		refresh_time = int(config.get("web","refresh_time"))

		return refresh_time
	except:
		return 30




def file_get_contents(file_name):
	try:
		with open(file_name) as f:
			return f.read()
	except Exception, e:
		print str(e)
		return None
	return None




def load_json_file(tm,refresh_time, suffix):

	global datadir


	q,r = divmod(tm.second,refresh_time)
	i = q * refresh_time
	if i == 60 : i = 0


	try :

		folder = tm.strftime(datadir + "/json-file/live/peer1/%Y/%m/%d/%H/")
		# folder = tm.strftime("/home/juyun/datafile/json-file/live/peer1/%Y/%m/%d/%H/")

		filename = tm.strftime("nfcapd.%Y%m%d%H%M") + "%0.2d." % i




		if testing :
			path = "/root/workspace/abcd/rawdata/nfcapd.20150109140000."
		else : 
			path = folder + filename


		# contents = file_get_contents(folder + filename + suffix)
		# contents = file_get_contents("/home/juyun/datafile/json-file/live/peer1/2014/12/19/10/nfcapd.20141219105930." + suffix)
		
		contents = file_get_contents(path+suffix)


		# print(path+suffix) 

		if contents is not None:
			return json.loads(contents)

	except : pass

	print(path+suffix + '  is not exists')
	return None



def format_newrelicdata_from_dictdata(dictdata):

	global pluginname

	header = """
	{
		"agent": {
			"host" : "test.clearclouds.com",
			"pid" : 1234,
			"version" : "1.0.0"
		},
		"components": [		
			{
				"name": "%s",
				"guid": "com.clearclouds.Clearclouds",
				"duration" : 60,
				"metrics" : {
					""" % (pluginname)



	footer = """
				}
			}
		]
	}
	"""


	strdata = ""
	seperator = ""
	# seperator = "					"
	i = 0 
	for firstkey,firstvalue in dictdata.items() :
		if i == 0 :
			strdata = seperator + '"' + firstkey + '" : ' + str(firstvalue)
		else :
			strdata = strdata + ',' + seperator + '"' + firstkey + '" : ' + str(firstvalue)

		i = i + 1 




	strdata =  header + strdata + footer
	# strdata =  (header + strdata + footer)   % (pluginname)




	# get_commandline() 
	# print(strdata)
	# sys.exit(1)


	return strdata






def parse_jsons(tm,refresh_time):

	data = {}
	dictdata = {}

	# tm = datetime.datetime.now()
	# tm = tm - datetime.timedelta(minutes = 1)

	# refresh_time = get_refresh_time()

	try :
		json_tcp = load_json_file(tm,refresh_time, "tcp_5s")
	except : pass

	try :
		json_tcp_connection_all = load_json_file(tm,refresh_time, "tcp_connection_all_5s")
	except : pass

	try :
		json_tcp_timeout = load_json_file(tm,refresh_time, "tcp_timeout_5s")	
	except : pass


	try :
		json_http = load_json_file(tm,refresh_time, "http_5s")
	except : pass

	try :
		json_http_status = load_json_file(tm,refresh_time, "http_status_5s")	
	except : pass

	try :	
		json_npm_traffic = load_json_file(tm,refresh_time, "npm_traffic_all_5s")
	except : pass

	try :
		json_npm_port = load_json_file(tm,refresh_time, "npm_port_all_5s")
	except : pass


	# try :
	# 	json_http_filter_url_status = load_json_file(tm,refresh_time, "http_filter_url_status_1m")
	# except : pass

	# try :
	# 	json_http_filter_url_delay = load_json_file(tm,refresh_time, "http_filter_url_5s")
	# except : pass

	try :
		json_http_filter_status = load_json_file(tm,refresh_time, "http_filter_status_5s")
	except : pass

	try :
		json_http_url_status = load_json_file(tm,refresh_time, "http_url_status_5s")
	except : pass

	try :
		json_http_url_delay = load_json_file(tm,refresh_time, "http_url_5s")
	except : pass

	try :
		json_http_apdex = load_json_file(tm,refresh_time, "http_url_5s")
	except : pass


	try :
		json_http_url = load_json_file(tm,refresh_time, "http_url_5s")
	except : pass




	
	dictdata = {}

	try :	
		pairdata = tcp.format_data_tcp(json_tcp,refresh_time)	
		dictdata.update(pairdata)
	except : pass

	try :	
		pairdata = tcpconn.format_data_tcp_connection(json_tcp_connection_all,refresh_time)	
		dictdata.update(pairdata)
	except : pass

	try :	
		pairdata = tcptimeout.format_data_tcp_timeout(json_tcp_timeout,refresh_time)
		dictdata.update(pairdata)
	except : pass

	try :	
		pairdata = http.format_data_http(json_http,refresh_time)	
		dictdata.update(pairdata)
	except : pass

	try :	
		pairdata = httpstatus.format_data_http_status(json_http_status,refresh_time)	
		dictdata.update(pairdata)
	except : pass

	try :	
		pairdata = traffic.format_data_npm_traffic(json_npm_traffic,refresh_time)
		dictdata.update(pairdata)
	except : pass


	# try :	
	# 	pairdata = httpfilterurlstatus.format_data_http_filter_url_status(json_http_filter_url_status,refresh_time)
	# 	dictdata.update(pairdata)
	# except : pass


	dumpdata = {}
	dumpdata = dumper.get_http_data(tm,refresh_time)

	try :	
		# pairdata = apdex.get_json_data_apdex(json_http_url_status)
		# pairdata = apdex.get_json_data_apdex2(json_http_url)
		pairdata = apdex.get_json_data_apdex(dumpdata)
		dictdata.update(pairdata)
	except : pass

	try :	
		pairdata = apdex.get_json_data_apdex_global(dumpdata)
		dictdata.update(pairdata)
	except : pass


	# try :	
	# 	pairdata = httpfilterurldelay.format_data_http_filter_url_delay(json_http_filter_url_delay,refresh_time)
	# 	dictdata.update(pairdata)
	# except : pass


	try :	
		# pairdata = httpurlstatus.format_data_http_url_status(json_http_url_status,refresh_time)
		pairdata = errorrate.get_json_data_errorrate(dumpdata) 
		dictdata.update(pairdata)
	except : pass

	try :	
		pairdata = errorrate.get_json_data_errorrate_global(dumpdata) 
		dictdata.update(pairdata)
	except : pass


	try :	
		# pairdata = httpurl.format_data_http_url(json_http_url,refresh_time)
		pairdata = httplatency.get_json_data_httplatency(dumpdata)
		dictdata.update(pairdata)
	except : pass


	try :	
		pairdata = httplatency.get_json_data_httplatency_global(dumpdata)
		dictdata.update(pairdata)
	except : pass




	data = format_newrelicdata_from_dictdata(dictdata)



	common.jprint(data)

	try :
		if testing:
			print("Testing") 
		else :

			result = post_newrelic(data)

			return result

	except : pass

	return False



def ExcuteFetcher(refresh_time):

	global testing
	
	loopcount = 0 

	handled = False

	get_commandline() 

	# sys.exit(1)


	while True:

		try :
			tm = datetime.datetime.now()
			
			tm = tm - datetime.timedelta(minutes = 1)

			if tm.second == 60 : 
				
				time.sleep(1)

				continue 

			flag =  ( (tm.second % refresh_time) > (refresh_time % 2) )



			if flag :

				if not handled :

					handled = parse_jsons(tm,refresh_time)

					loopcount = loopcount + 1 

					if loopcount > 5 :

						handled = True

						loopcount = 0 
							

			else:

				handled = False;

			time.sleep(1)

		except : continue


	return 0





def main():	

	refresh_time = get_refresh_time()

	if refresh_time  > 4  and refresh_time <= 60 : 

		analyse_commandline(refresh_time)

	else :

		print('refresh_time should between 4s and 60s ')




if __name__ == '__main__':

	main()


# main()

# exit(main())