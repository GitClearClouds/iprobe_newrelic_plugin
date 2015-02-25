#! /usr/bin/env python

import sys
import os
import ConfigParser
import getopt


datadir = '/home/juyun/datafile'
newrelickey = '19e4cb7a2ec9c43a7a90cec3360fb7b5868d08d6'
pluginname = 'ClearClouds'
juyuninidir = '/usr/local/etc'
juyunini_newrelic = '/usr/local/etc/newrelic.ini'



def usage():  
	print("Usage:%s [-d|-k|-n] [--help|--output] args...." % sys.argv[0]);  
	print("-d datadir");  
	print("-k new relic license key");  
	print("-n plugin id ");  




def analyse_commandline() :

	try :
		opts,args = getopt.getopt(sys.argv[1:], "d:k:n:", ["help"])


		for opt,arg in opts:  

			if opt in ("-h", "--help"):

				usage()
				sys.exit(1);  

			elif opt in ("-t", "--test"):

				print("for test option");

			elif opt in ("-d") :

				dodir(arg) 

			elif opt in ("-k") :

				dokey(arg)


			elif opt in ("-n") :

				doname(arg)


			else:
				print("%s  ==> %s" %(opt, arg))


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

			f = open(juyunini_newrelic,'rw')
			f.write('[newrelic]\n')
			f.write('datadir = ')
			f.write('newrelickey = ')
			f.write('pluginname = ')
			f.write(sys.argv[1])
			f.close()


		config = ConfigParser.ConfigParser()
		config.read(juyunini_newrelic)
		# config.set("newrelic","datadir",key)
		config.set("newrelic","newrelickey",key)
		# config.set("newrelic","pluginname",key)
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

			f = open(juyunini_newrelic,'rw')
			f.write('[newrelic]\n')
			f.write('datadir = ')
			f.write('newrelickey = ')
			f.write('pluginname = ')
			f.write(sys.argv[1])
			f.close()


		config = ConfigParser.ConfigParser()
		config.read(juyunini_newrelic)
		config.set("newrelic","datadir",key)
		# config.set("newrelic","newrelickey",key)
		# config.set("newrelic","pluginname",key)
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

			f = open(juyunini_newrelic,'rw')
			f.write('[newrelic]\n')
			f.write('datadir = ')
			f.write('newrelickey = ')
			f.write('pluginname = ')
			f.write(sys.argv[1])
			f.close()


		config = ConfigParser.ConfigParser()
		config.read(juyunini_newrelic)
		# config.set("newrelic","datadir",key)
		# config.set("newrelic","newrelickey",key)
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





def ssssssss() :

	global juyuninidir
	global juyunini_newrelic

	try :

		if len(sys.argv) < 1 : print('no key!')

		if not os.path.exists(juyuninidir) :

			dumpcommand = 'mkdir -p '+ juyuninidir

			os.popen(dumpcommand)


		if not os.path.exists(juyunini_newrelic) :

			f = open(juyunini_newrelic,'rw')
			f.write('[newrelic]\n')
			f.write('newrelickey = ')
			f.write(sys.argv[1])
			f.close()

		else :

			config = ConfigParser.ConfigParser()
			config.read(juyunini_newrelic)
			config.set("newrelic","newrelickey",sys.argv[1])
			config.write(open(juyunini_newrelic,'w'))

	except : pass






def main():
	analyse_commandline()

if __name__ == '__main__':
	main()

