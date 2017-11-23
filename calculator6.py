#!/usr/bin/env python3

import sys
import os
import getopt
import configparser
from datetime import datetime
from multiprocessing import Process,Queue
from decimal import Decimal


queue1 = Queue()
queue2 = Queue()

def salary(userdatafile):
    userdata = {}
    try:
        if len(sys.argv)>0 and os.path.isfile(userdatafile):
            f = open(userdatafile)
            for user in f:
                user = user.strip('\n')
                user = user.split(',')
                key = user[0].strip()
                value = user[1].strip()
                userdata[key] = value
            print(userdata)
    except:
        raise
    queue1.put(userdata)


def tax_due(configfile_list):
    userdata = queue1.get()
    config = []
    for i,r in configfile_list:
        config.append(Decimal(r))
    rate = float(sum(config[2:]))
    
    ID = []
    MS = []
    SI = []
    IIT = []
    AT = []
    TDI = []

    for info1 in userdata.keys():
        ID.append(int(info1))
    for info2 in userdata.values():
        MS.append(int(info2))
    for wage in MS:
        if wage < config[0]:
            si = 2193 * rate
        elif wage > config[1]:
            si = 16446 * rate
        else:
            si = wage * rate
        tdi = wage - si - 3500 
        SI.append(float('%.2f'%si))        
        TDI.append(tdi)
    for tdi in TDI:
        if tdi <= 0:
            iit = 0.00
        elif tdi <= 1500:
            iit  = tdi*0.03-0
        elif tdi <= 4500:
            iit = tdi*0.10-105
        elif tdi <= 9000:
            iit = tdi*0.20-555
        elif tdi <= 35000:
            iit = tdi*0.25-1005
        elif tdi <= 55000:
            iit = tdi*0.30-2755
        elif tdi <= 80000:
            iit = tdi*0.35-5505
        else:
            iit = tdi*0.45-13505
        IIT.append(float('%.2f'%iit))
    for i in range(len(ID)):
        at = MS[i] - SI[i] - IIT[i]
        AT.append('%.2f'%at)
    newdata = zip(ID, MS, SI, IIT, AT)
    queue2.put(newdata)


def write(resultdata):
    newdata = queue2.get()
    t = datetime.now()
    T = datetime.strftime(t, '%Y-%m-%d %H:%M:%S')
    f = open(resultdata, 'a')
    for sub_data in newdata:
        for sub_info in sub_data:      
            f.write(str(sub_info))
            f.write(',')
        f.write(',')
        f.write(T)
        f.write('\n\n')
    f.close()


def main():
    argv = sys.argv[1:]
    cityname = ''
    configfile = ''
    userdatafile = ''
    resultdata = ''
    try:
        opts,args = getopt.getopt(argv,'hC:c:d:o:',['help','cityname=','configfile=','userdatafile=','resultdata=']) 
        print(opts,args)
    except:
        raise
    for opt,arg in opts:
        if opt in ('-h','--help'):
            usage()
            sys.exit()
        elif opt in ('-C','--cityname'):
            cityname = arg
        elif opt in ('-c','--configfile'):
            configfile = arg
        elif opt in ('-d','--userdatafile'):
            userdatafile = arg
        elif opt in ('-o','--resultdata'):
            resultdata = arg
        else:
            print('Wrong')
    config = configparser.ConfigParser()
    config.read(configfile)
    try:
        if not cityname:
            cityname = 'DEFAULT'
            configfile_list = (config.defaults()).items()
        else:
            cityname = cityname.upper()
            list_headers = config.sections()
            if cityname in list_headers:
                configfile_list = config.items(cityname)
            else:
                raise
    except:
        raise

    p1 = Process(target=salary, args=(userdatafile,))
    p2 = Process(target=tax_due, args=(configfile_list,))
    p3 = Process(target=write, args=(resultdata,))
    p1.start()
    p2.start()
    p3.start()
        

if __name__ == '__main__':
    main()
             
                 
