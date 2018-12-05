# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 12:03:50 2018

@author: tyagi
"""

def banyan1x1(inpt):
    oupt = ["",""]
    if inpt[0] == 0:
        oupt[0] = inpt[1:]
    else:
       oupt[1] = inpt[1:]
    return oupt

print(banyan1x1([1,"fkjsdfhkjsdf"]))
        