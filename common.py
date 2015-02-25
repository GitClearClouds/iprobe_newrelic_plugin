#! /usr/bin/env python

import sys
import os
import time
import json
import string
import datetime
import random
import re
import commands



istest = False



def jprint(data):

	if getistest() : 
		print(data)


def setistest(val):

	global istest

	istest = val



def getistest():

	global istest
	
	return istest