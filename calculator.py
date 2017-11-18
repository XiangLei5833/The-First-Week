#!/usr/bin/env python4

import sys

def Social_security(salary):
    tax_rate = 0.08+0.02+0.005+0.06
    ss = salary * tax_rate
    return ss

def Tax_due_income(salary, ss):
    Tdi = salary - ss - 3500
    while Tdi > 0:
        return Tdi
    else:
        return None

def Tax_due(Tdi, ss):
    if Tdi == None:
        Td = ss
    elif Tdi <= 1500:
        Td = Tdi * 0.03 - 0 + ss
    elif Tdi <= 4500:
        Td = Tdi * 0.1 - 105 + ss
    elif Tdi <= 9000:
        Td = Tdi * 0.2 - 555 + ss
    elif Tdi <= 35000:
        Td = Tdi * 0.25 - 1005 + ss
    elif Tdi <= 55000:
        Td = Tdi * 0.3 - 2755 + ss
    elif Tdi <= 80000:
        Td = Tdi * 0.35 - 5505 + ss
    else:
        Td = Tdi * 0.45 - 13505 + ss
    return Td

def main():
    try:
        sa = sys.argv
        sav = sa[1:]
        if len(sa) > 0:
            for arg in sav:
                j_number = int((arg.split(':'))[0])
                salary = int((arg.split(':'))[1])
                ss = Social_security(salary)
                Tdi = Tax_due_income(salary, ss)
                Td = Tax_due(Tdi, ss)
                take_home_salary = salary - Td
                print('%d:%.2f'%(j_number,take_home_salary))
        else:
            raise
    except:
        print('Parameter Error')
   

if __name__ == '__main__':
    main()
