#! /usr/bin/env python

import time
import string
from datetime import datetime as dt
import re
import dumper
import common


valvel = 7000000
valveh = 28000000   


def get_json_data_apdex(dumpdata):

    global valvel
    global valveh

    # dumpdata = {}
    url_satisfied_count = {}
    url_tolerating_count  = {}
    url_frustrated_count  = {}


    # dumpdata = dumper.get_http_data(tm)

    for item in dumpdata :

        iteminner = item.split()

        url = iteminner[11]
        data = int(iteminner[8])
        status = int(iteminner[9])

        if status >= 400 :

            data = 999999999

            # if url in url_frustrated_count :

            #     url_frustrated_count[url]++
                
            # else :

            #     strdata = '{"%s":1}' % (url)
            #     dictdata = eval(strdata)
            #     url_frustrated_count.update(dictdata)   

            # continue


        if data <= valvel :

            if url in url_satisfied_count :

                url_satisfied_count[url] = url_satisfied_count[url] + 1                 
                # url_satisfied_count[url]++
            else :

                strdata = '{"%s":1}' % (url)
                dictdata = eval(strdata)
                url_satisfied_count.update(dictdata)

                
        elif data > valveh :

            if url in url_frustrated_count :

                url_frustrated_count[url] = url_frustrated_count[url] + 1 
                # url_frustrated_count[url]++
                
            else :

                strdata = '{"%s":1}' % (url)
                dictdata = eval(strdata)
                url_frustrated_count.update(dictdata)               


        else :

            if url in url_tolerating_count :

                url_tolerating_count[url] = url_tolerating_count[url] + 1     
                # url_tolerating_count[url]++            

            else :

                strdata = '{"%s":1}' % (url)
                dictdata = eval(strdata)
                url_tolerating_count.update(dictdata)               



    resultdata = {}
    tempdata = {}

    tempdata.update(url_satisfied_count)
    tempdata.update(url_tolerating_count)
    tempdata.update(url_frustrated_count)


    for url,value in tempdata.items() :

        if re.match(".*.jsp$",url) == None and re.match(".*.php$",url) == None : continue

        jsondata = {}

        a = 0 
        b = 0 
        c = 0

        if url in url_satisfied_count : 
            a =  a + url_satisfied_count[url] 
            b =  b + url_satisfied_count[url] 

        if url in url_tolerating_count : 
            a =  a + url_tolerating_count[url] / 2
            b =  b + url_tolerating_count[url] 

        if url in url_frustrated_count : 
            b =  b + url_frustrated_count[url] 

        if b > 0 : c = a/b*100


        if c < 99.999 :
            strdata =  '{"Component/Apdex/%s":%f}' % (url,c )
            jsondata = eval(strdata)
            resultdata.update(jsondata)



    return resultdata




def get_json_data_apdex_global(dumpdata):

    global valvel
    global valveh

    # dumpdata = {}
    url_satisfied_count = 0
    url_tolerating_count  = 0
    url_frustrated_count  = 0

    # dumpdata = dumper.get_http_data(tm)

    for item in dumpdata :

        iteminner = item.split()

        url = iteminner[11]
        data = int(iteminner[8])
        status = int(iteminner[9])

        if status >= 400 :

            data = 999999999


        if data <= valvel :
 
            url_satisfied_count = url_satisfied_count + 1


        elif data > valveh :

            url_frustrated_count = url_frustrated_count + 1

        else :
 
            url_tolerating_count = url_tolerating_count + 1



    resultdata = {}
    jsondata = {}


    good = url_satisfied_count + url_tolerating_count / 2
    sumcount = url_satisfied_count + url_frustrated_count + url_tolerating_count


    rate = 0 
    if sumcount > 0 : rate = good/sumcount  * 100


    strdata =  '{"Component/Http/Global/Apdex":%f}' % ( rate )
    jsondata = eval(strdata)
    resultdata.update(jsondata)


    common.jprint('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$4')
    common.jprint(resultdata)


    return resultdata




def get_json_data_apdex2(json_http_url):

    interval = 500000
    interval = 7000000
    latencyisavg = True

    resultdata = {}
    firstdata = {}
    seconddata = {}
    thirddata = {}
    alldata = []
    nonalldata = []
    resultdata = {}
    url_requests_inall = {}
    url_apdex = {}
    url_errorrate = {}

    url_satisfied = {}
    url_tolerating = {}
    url_frustrated = {}

    totalrequest = 0
###############################################################################
    hascalc = False
    for firstkey,firstvalue in json_http_url.items() :

        if firstkey != 'requests' : continue

        if hascalc == True : break

        hascalc = True

        for secondkey,secondvalue in firstvalue.items() :

            if secondkey != 'all' : continue

            alldata.extend(secondvalue)


    for item in alldata :

        tempdata = {}

        strdata =  '{"%s":%d}' % (item['url'] ,item['requests'] )

        tempdata = eval(strdata)

        # print(tempdata)

        if item['url'] in url_requests_inall :

            url_requests_inall[item['url']] += item['requests']

        else :

            url_requests_inall.update(tempdata)

    # print (url_requests_inall)
##############################################################################

###############################################################################
    nonalldata = []
    hascalc = False

    for firstkey,firstvalue in json_http_url.items() :

        if firstkey != 'requests' : continue

        if hascalc == True : break

        hascalc = True

        for secondkey,secondvalue in firstvalue.items() :

            if secondkey == 'all' : continue

            nonalldata.extend(secondvalue)

    for item in nonalldata :
        satisfied = 0
        tolerating = 0
        frustrated = 0
        strdata =  '{"%s":%d}' % (item['url'] ,item['requests'] )
        tempdata = {}
        tempdata = eval(strdata)

        if latencyisavg : 
            coof = interval
        else :
            coof = interval * item['requests'] 


        if item['latency'] <= coof :
            if item['url'] in url_satisfied :
                url_satisfied[item['url']] += item['requests']
            else :
                url_satisfied.update(tempdata)
        elif item['latency'] >  4 * coof :
            if item['url'] in url_frustrated :
                url_frustrated[item['url']] += item['requests']
            else :
                url_frustrated.update(tempdata)
        else :
            if item['url'] in url_tolerating :
                url_tolerating[item['url']] += item['requests']
            else :
                url_tolerating.update(tempdata)


    # print (url_frustrated)
##############################################################################


###############################################################################
    # print (alldata)
    satisfied = 0
    tolerating = 0
    frustrated = 0

    for item in alldata :

        if re.match(".*.php$",item['url']) == None : continue

        if item['url'] in url_satisfied :
            satisfied += url_satisfied[item['url']]
        elif item['url'] in url_tolerating :
            tolerating += url_tolerating[item['url']]
        elif item['url'] in url_frustrated :
            frustrated += url_frustrated[item['url']]

        total_number = satisfied + tolerating + frustrated

        if total_number == 0 : continue
        

        apdex = (satisfied + tolerating / 2) * 100 / total_number

        tempdata = {}
        strdata =  '{"Component/Apdex/%s":%f}' % (item['url'] ,apdex )
        tempdata = eval(strdata)
        url_apdex.update(tempdata)


        

        # print(tempdata)


    return url_apdex



def get_json_data_apdex3(json_http_url):

    interval = 500000
    resultdata = {}
    firstdata = {}
    seconddata = {}
    thirddata = {}
    alldata = []
    nonalldata = []
    resultdata = {}
    url_requests_inall = {}
    url_apdex = {}
    url_errorrate = {}

    url_satisfied = {}
    url_tolerating = {}
    url_frustrated = {}

    totalrequest = 0
###############################################################################
    hascalc = False
    for firstkey,firstvalue in json_http_url.items() :

        if firstkey != 'requests' : continue

        if hascalc == True : break

        hascalc = True

        for secondkey,secondvalue in firstvalue.items() :

            if secondkey != 'all' : continue

            alldata.extend(secondvalue)


    for item in alldata :

        tempdata = {}

        strdata =  '{"%s":%d}' % (item['url'] ,item['requests'] )

        tempdata = eval(strdata)

        # print(tempdata)

        if item['url'] in url_requests_inall :

            url_requests_inall[item['url']] += item['requests']

        else :

            url_requests_inall.update(tempdata)

    # print (url_requests_inall)
##############################################################################

###############################################################################
    nonalldata = []
    hascalc = False

    for firstkey,firstvalue in json_http_url.items() :

        if firstkey != 'requests' : continue

        if hascalc == True : break

        hascalc = True

        for secondkey,secondvalue in firstvalue.items() :

            if secondkey == 'all' : continue

            nonalldata.extend(secondvalue)

    for item in nonalldata :
        satisfied = 0
        tolerating = 0
        frustrated = 0
        strdata =  '{"%s":%d}' % (item['url'] ,item['requests'] )
        tempdata = {}
        tempdata = eval(strdata)


        if item['latency'] <= interval * item['requests'] :
            if item['url'] in url_satisfied :
                url_satisfied[item['url']] += item['requests']
            else :
                url_satisfied.update(tempdata)
        elif item['latency'] >  4 * interval * item['requests'] :
            if item['url'] in url_frustrated :
                url_frustrated[item['url']] += item['requests']
            else :
                url_frustrated.update(tempdata)
        else :
            if item['url'] in url_tolerating :
                url_tolerating[item['url']] += item['requests']
            else :
                url_tolerating.update(tempdata)

    # print (url_frustrated)
##############################################################################


###############################################################################
    # print (alldata)
    satisfied = 0
    tolerating = 0
    frustrated = 0

    for item in alldata :

        if re.match(".*.php$",item['url']) == None : continue

        if item['url'] in url_satisfied :
            satisfied += url_satisfied[item['url']]
        elif item['url'] in url_tolerating :
            tolerating += url_tolerating[item['url']]
        elif item['url'] in url_frustrated :
            frustrated += url_frustrated[item['url']]

        total_number = satisfied + tolerating + frustrated

        if total_number == 0 : continue
        

        apdex = (satisfied + tolerating / 2) * 100 / total_number

        tempdata = {}
        strdata =  '{"Component/Apdex/%s":%f}' % (item['url'] ,apdex )
        tempdata = eval(strdata)
        url_apdex.update(tempdata)


        

        # print(tempdata)


    return url_apdex