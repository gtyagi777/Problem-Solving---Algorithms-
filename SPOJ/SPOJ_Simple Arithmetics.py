# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 23:50:46 2018

@author: tyagi
"""

def printArithmatic(strng):
    if '+' in strng :
        x,y = strng.split('+')
        n = max(len(x),len(y)) + 1
        res = long(x)+ long(y)
        _count = len(str(res))
        
        print(x.rjust(n))
        print (("+"+y).rjust(n))
        print(("-"*_count).rjust(n))
        print(str(res).rjust(n))
    
    elif '-' in strng :
        x,y = strng.split('-')
        n = max(len(x),len(y)) + 1
        res = int(x) - int(y)
        _count = len(str(res))
        
        print(x.rjust(n))
        print (("-"+y).rjust(n))
        print(("-"*_count).rjust(n))
        print(str(res).rjust(n))
    
    elif '*' in strng:
        x,y = strng.split('*')
        n = len(y)+1
        res = int(x) * int(y)
        res = str(res)
        just = len(res)
        print(x.rjust(just))
        print (("*"+y).rjust(just))
        
        if len(y) > 1:
            if y == '99':
                print(("-"*len(x)).rjust(just))
            else:
                print(("-"*n).rjust(just))
            y = int(y)
            for i in range(len(str(y))):
                mult = y %10 
                y = y//10
                res_ = int(x) * int(mult)
                print(str(res_).rjust(just-i))
            print(("-"*just).rjust(just))
            print(res.rjust(just))
        else:
            print(("-"*just).rjust(just))
            print(res.rjust(just))
    print()
            
        

#driver program
printArithmatic("9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999*9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999")        