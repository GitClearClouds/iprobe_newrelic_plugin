#! /usr/bin/env python

import time
import string
from datetime import datetime as dt
import re
import dumper
import common



def get_json_data_errorrate(dumpdata):

    # dumpdata = {}
    url_status_count_1xx = {}
    url_status_count_2xx  = {}
    url_status_count_3xx = {}
    url_status_count_4xx  = {}
    url_status_count_5xx  = {}
    url_status_count_other  = {}


    # dumpdata = dumper.get_http_data(tm)

    for item in dumpdata :

        iteminner = item.split()

        url = iteminner[11]
        data = int(iteminner[9])


        if data >= 100 and data < 200 :

            if url in url_status_count_1xx :

                url_status_count_1xx[url] = url_status_count_1xx[url] + 1 

            else :

                strdata = '{"%s":1}' % (url)
                dictdata = eval(strdata)
                url_status_count_1xx.update(dictdata)             


        elif data >= 200 and data < 300 :

            if url in  url_status_count_2xx :

                url_status_count_2xx[url] = url_status_count_2xx[url] + 1                 

            else :

                strdata = '{"%s":1}' % (url)
                dictdata = eval(strdata)
                url_status_count_2xx.update(dictdata)
                


        elif data >= 300 and data < 400 :

            if url in  url_status_count_3xx :

                url_status_count_3xx[url] = url_status_count_3xx[url] + 1                 

            else :
                strdata = '{"%s":1}' % (url)
                dictdata = eval(strdata)
                url_status_count_3xx.update(dictdata)
                

        elif data >= 400 and data < 500 :

            if url in  url_status_count_4xx :

                url_status_count_4xx[url] = url_status_count_4xx[url] + 1 

            else :
                strdata = '{"%s":1}' % (url)
                dictdata = eval(strdata)
                url_status_count_4xx.update(dictdata)
                

        elif data >= 500 and data < 600 :

            if url in  url_status_count_5xx :

                url_status_count_5xx[url] = url_status_count_5xx[url] + 1 

            else :

                strdata = '{"%s":1}' % (url)
                dictdata = eval(strdata)
                url_status_count_5xx.update(dictdata)   


        else :

            if url in url_status_count_other :

                url_status_count_other[url] = url_status_count_other[url] + 1                 

            else :

                strdata = '{"%s":1}' % (url)
                dictdata = eval(strdata)
                url_status_count_other.update(dictdata)
                



    resultdata = {}
    tempdata = {}

    tempdata.update(url_status_count_1xx)
    tempdata.update(url_status_count_2xx)
    tempdata.update(url_status_count_3xx)
    tempdata.update(url_status_count_4xx)
    tempdata.update(url_status_count_5xx)
    tempdata.update(url_status_count_other)



    for url,value in tempdata.items() :

        jsondata = {}

        error = 0 
        sumcount = 0 
        rate = 0

        if re.match(".*.jsp$",url) == None and re.match(".*.php$",url) == None : continue


        if  url in url_status_count_1xx : 

            sumcount = sumcount + url_status_count_1xx[url] 
            error = error + url_status_count_1xx[url] 

        if url in url_status_count_2xx : 

            sumcount = sumcount + url_status_count_2xx[url] 
            
        if url in url_status_count_3xx : 

            sumcount = sumcount + url_status_count_3xx[url] 

        if url in url_status_count_4xx : 

            sumcount = sumcount + url_status_count_4xx[url] 
            error = error + url_status_count_4xx[url] 

        if url in url_status_count_5xx : 

            sumcount = sumcount + url_status_count_5xx[url] 
            error = error + url_status_count_5xx[url] 

        if url in url_status_count_other : 

            sumcount = sumcount + url_status_count_other[url]   
            error = error + url_status_count_other[url]   


        if sumcount > 0 : rate = error/sumcount *100

        if rate > 0.001 :

            strdata =  '{"Component/Error rate/%s":%f}' % (url,rate )
            jsondata = eval(strdata)
            resultdata.update(jsondata)

    


    return resultdata





def get_json_data_errorrate_global(dumpdata):

    # dumpdata = {}
    url_status_count_1xx = 0
    url_status_count_2xx  = 0
    url_status_count_3xx = 0
    url_status_count_4xx  = 0
    url_status_count_5xx  = 0
    url_status_count_other  = 0

    resultdata = {}


    # dumpdata = dumper.get_http_data(tm)

    for item in dumpdata :

        iteminner = item.split()

        url = iteminner[11]
        data = int(iteminner[9])


        if data >= 100 and data < 200 :

            # url_status_count_1xx++
            url_status_count_1xx = url_status_count_1xx + 1


        elif data >= 200 and data < 300 :

            # url_status_count_2xx++
            url_status_count_2xx = url_status_count_2xx + 1


        elif data >= 300 and data < 400 :

            # url_status_count_3xx++
            url_status_count_3xx = url_status_count_3xx + 1
                

        elif data >= 400 and data < 500 :

            # url_status_count_4xx++
            url_status_count_4xx = url_status_count_4xx + 1
                

        elif data >= 500 and data < 600 :

            # url_status_count_5xx++
            url_status_count_5xx = url_status_count_5xx + 1


        else :

            # url_status_count_other++
            url_status_count_other = url_status_count_other + 1
                


    rate = 0 
    
    error = url_status_count_4xx + url_status_count_5xx + url_status_count_other ;

    sumcount = (url_status_count_1xx + url_status_count_2xx + url_status_count_3xx
                + url_status_count_4xx + url_status_count_5xx + url_status_count_other )


    if sumcount > 0 : rate = error/sumcount * 100


    strdata =  '{"Component/Http/Global/ErrorRate":%f}' % (rate )
    jsondata = {}
    
    jsondata = eval(strdata)
    resultdata.update(jsondata)



    common.jprint('*****************************************************************************')
    common.jprint(resultdata)


    return resultdata