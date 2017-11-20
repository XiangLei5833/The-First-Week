#!/usr/bin/env python3

import sys
import os
args = sys.argv[1:]
index = args.index('-c')
configfile = args[index+1]
index = args.index('-d')
userdatafile = args[index+1]

class Config(object):
    def __init__(self, configfile):
        self._configfile = configfile
        self._config = {}
        try:
            if len(sys.argv)>0 and os.path.isfile(self._configfile) :
                f = open(self._configfile, 'r')
                for c in f:
                    c = c.strip('\n')
                    c = c.split('=')
                    key = c[0].strip()
                    value = c[1].strip()
                    self._config[key] = value
            else:
                raise
        except:
              raise
    def get_config(self):
        return self._config

class UserData(object):
    def __init__(self, userdatafile):
        self._userdatafile = userdatafile
        self._userdata = {}
        try:
            if len(sys.argv)>0 and os.path.isfile(self._userdatafile):
                f = open(self._userdatafile, 'r')
                for u in f:
                    u = u.strip('\n')
                    u = u.split(',')
                    key = u[0].strip()
                    value = u[1].strip()
                    self._userdata[key] = value
            else:
                raise
        except:
            raise
    def get_userdata(self):
        return self._userdata

class Salary(object):
    def social_security(self, salary, rate):
        R = []
        for r in rate:
            r = float(r)
            if r < 1:
               R.append(r)
        r = sum(R)
        if salary < 2193:
            ss = 2193.00 * r
        elif salary > 16446:
            ss = 16446.00 * r
        else:
            ss = salary * r
            ss = float(ss)
        return ss
    def tax_due_income(self, salary, ss):
        tdi = salary - ss - 3500
        while tdi > 0:
            return tdi
        else:
            return None
    def tax_due(self, tdi, ss):
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
    def main(self):
        C = Config(configfile)
        rate = list((C.get_config()).values())
        U = UserData(userdatafile)
        j_number = (U.get_userdata()).keys()
        self_userdata = U.get_userdata()
        for num in j_number:
            salary = int(self_userdata[num])
            ss = self.social_security(salary,rate)
            tdi = self.tax_due_income(salary, ss)
            td = self.tax_due(tdi, ss)
            pit = float(td-ss)
            ths = float(salary-td)
            num = int(num)
            try:
                if len(sys.argv) > 0:
                    args = sys.argv[1:]
                    index = args.index('-o')
                    gongzi = args[index+1]
                    f = open(gongzi, 'a')
                    f.writelines('%d,%d,%.2f,%.2f,%.2f'% (num, salary, ss, pit, ths))
                    f.write('\n\n')
                else:
                    raise
            except:
                raise
        f.close()

if __name__ == '__main__':
    s = Salary()
    s.main()
   
