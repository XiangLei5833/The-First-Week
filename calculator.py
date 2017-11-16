#!/usr/bin/env python3

import sys

try:
    if len(sys.argv) == 2:
        Salary = int(sys.argv[1])
        Tds = Salary - 0 - 3500
        if Tds <= 0:
            Td = 0.0
        elif Tds <= 1500:
            Td = Tds * 0.03 - 0
        elif Tds <= 4500:
            Td = Tds * 0.1 - 105
        elif Tds <= 9000:
            Td = Tds * 0.2 - 555
        elif Tds <= 35000:
            Td = Tds * 0.25 - 1005
        elif Tds <= 55000:
            Td = Tds * 0.30 - 2755
        elif Tds <= 80000:
            Td = Tds * 0.35 - 5505
        else:
            Td = Tds * 0.45 - 13505
        print('{:.2f}'.format(Td))
except:
    print('Parameter Error')
