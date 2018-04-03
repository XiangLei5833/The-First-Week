#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import pdb

logging.basicConfig(level=logging.INFO)    # 允许指定记录信息的级别：debug, info, waring, wrror，由低到高依次排列，指定高级别的就会对低级别进行覆盖

s = '0'
n = int(s)
pdb.set_trace()
logging.info('n = %d' % n)
print(10/n)
