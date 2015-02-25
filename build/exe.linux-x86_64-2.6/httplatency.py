#! /usr/bin/env python

import time
import string
from datetime import datetime as dt
import re
import dumper
import common



def get_json_data_httplatency(dumpdata):

    # dumpdata = {}
    url_latency = {}
    url_count = {}


    # dumpdata = dumper.get_http_data(tm)

    for item in dumpdata :

        iteminner = item.split()

        url = iteminner[11]
        data = int(iteminner[8])


        if url in url_latency :

            url_latency[url] = url_latency[url] + data

        else :
            strdata = '{"%s":%d}' % (url,data)
            dictdata = eval(strdata)
            url_latency.update(dictdata)

            


        if url in url_count :

            url_count[url] = url_count[url] + 1
            
        else :

            strdata = '{"%s":%d}' % (url,1)
            dictdata = eval(strdata)
            url_count.update(dictdata)            



    resultdata = {}



    for url,count in url_count.items() :

        jsondata = {}

        sumlatency = 0 
        avglatency = 0

        if count == 0 : continue

        if re.match(".*.jpg$",url) == None and re.match(".*.php$",url) == None : continue        

        if not url in url_latency : continue


        sumlatency = url_latency[url]

        avglatency = sumlatency/count


        strdata =  '{"Component/Url/Latency/%s":%f}' % (url,avglatency)
        jsondata = eval(strdata)
        resultdata.update(jsondata)

    

    return resultdata




def get_json_data_httplatency_global(dumpdata):

    # dumpdata = {}
    # dumpdata = dumper.get_http_data(tm)
    print('get_json_data_httplatency_global')

    url_latency = 0
    url_count = 0


    for item in dumpdata :

        iteminner = item.split()

        url = iteminner[11]
        data = int(iteminner[8])

        url_latency = url_latency + data
        url_count = url_count + 1

    resultdata = {}

    avglatency = 0.0 

    if url_count > 0 :
        avglatency = url_latency/url_count/1000000


        strdata =  '{"Component/Http/Global/Latency":%.8f}' % (avglatency)
        jsondata = eval(strdata)
        resultdata.update(jsondata)


    common.jprint('----------------------------------------------------------------------------------------')
    common.jprint(url_latency)
    common.jprint(resultdata)

    return resultdata