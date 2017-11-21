#!/usr/bin/env python3

import sys
import os

class Config(object):
    def __init__(self, configfile):
        self._config = {}
        try:
            if len(sys.argv)>0 and os.path.isfile('/home/shiyanlou/test.cfg') :
                args = sys.argv[1:]
                index = args.index('-c')
                configfile = args[index+1]
                f = open(configfile, 'r')
                for c in f:
                    c = c.strip('\n')
                    c = c.split('=')
                    key = c[0]
                    value = c[1]
                    self._config[key] = value
            else:
                raise
        except:
              raise
    def get_config(self):
        return self.config

class UserData(object):
    def __init__(self, userdatafile):
        self._userdata = {}
        try:
            if len(sys.argv)>0 and os.path.isfile('/home/shiyanlou/user.csv'):
                args = sys.argv[1:]
                index = args.index('-d')
                userdatafile = args[index+1]
                f = open(userdatafile, 'r')
                for u in f:
                    u = u.strip('\n')
                    u = u.split(':')
                    key = u[0]
                    value = u[1]
                    self._userdata[key] = value
            else:
                raise
        except:
            raise
    def get_userdata(self):
        return self._userdata

class Salary(object):
    C = Config()
    U = UserData()
    rate = C.get_config().values()
    j_number = U.get_userdata().keys()
    def social_security(salary):
        for r in rate[2:]:
            r = int(r)
            r += r
            return r
        if salary < rate[0]:
            ss = 2193.00 * r
        elif salary > rate[1]:
            ss = 16446.00 * r
        else:
            ss = salary * r
            ss = '%.2f'%(ss)
        return ss
    def tax_due_income(salary, ss):
        tdi = salary - ss - 3500
        while tdi > 0:
            return tdi
        else:
            return None
    def tax_due(tdi, ss):
        if tdi == None:
            td = ss
        elif tdi <= 1500:
            td = tdi * 0.03 - 0 + ss
        elif tdi <= 4500:
            td = tdi * 0.1 - 105 + ss
        elif tdi <= 9000:
            td = tdi * 0.2 - 555 + ss
        elif tdi <= 35000:
            td = tdi * 0.25 - 1005 + ss
        elif tdi <= 55000:
            td = tdi * 0.3 - 2755 + ss
        elif tdi <= 80000:
            td = tdi * 0.35 - 5505 + ss
        else:
            td = tdi * 0.45 - 13505 + ss
        return td
    def main():
        for num in j_number:
            num = int(num)
            salary = int(self._userdata[num])
            ss = social_security(salary)
            tdi = tax_due_income(salary, ss)
            td = tax_due(tdi, ss)
            pit = '%.2f'%(td-ss)
            ths = '%.2f'%(salary-td)
            try:
                if len(sys.argv) > 0:
                    args = sys.argv[1:]
                    index = args.index('-o')
                    gongzi = args[index+1]
                    f = open(gongzi, 'w')
                    f.write('%d%d%f%f%f' % (num, salary, ss, pit, ths))
                else:
                    raise
            except:
                raise
        f.close()
if __name__ == '__main__':
    s = Salary(object)
    s.main()   
