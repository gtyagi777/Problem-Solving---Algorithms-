# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 21:43:09 2018

@author: tyagi
"""

import random


def switchAtoB(input, dest):

    if input == 'A1':
        if dest[0] == '0':
	        path2 = 'B1'
        else:
	        path2 = 'B3'


    if input == 'A2':
	    if dest[0] == '0':
		    path2 = 'B2'
	    else:
		    path2 = 'B4'

    if input == 'A3':
	    if dest[0] == '0':
		    path2 = 'B1'
	    else:
		    path2 = 'B3'

    if input == 'A4':
	    if dest[0] == '0':
		    path2 = 'B2'
	    else:
		    path2 = 'B4'
    return path2


def switchBtoC(input, dest):

    if input == 'B1':
        	if dest[1] == '0':
                    	path3 = 'C1'
        	else:
                    	path3 = 'C2'


    if input == 'B2':
        	if dest[1] == '0':
                    	path3 = 'C1'
        	else:
                    	path3 = 'C2'

    if input == 'B3':
        	if dest[1] == '0':
                    	path3 = 'C3'
        	else:
                    	path3 = 'C4'

    if input == 'B4':
        	if dest[1] == '0':
                    	path3 = 'C3'
        	else:
                    	path3 = 'C4'

    return path3


def switchCtoOutput(input, dest):

    if input == 'C1':
        	if dest[2] == '0':
                    	path4 = '0'
        	else:
                    	path4 = '1'


    if input == 'C2':
        	if dest[2] == '0':
                    	path4 = '2'
        	else:
                    	path4 = '3'

    if input == 'C3':
        	if dest[2] == '0':
                    	path4 = '4'
        	else:
                    	path4 = '5'

    if input == 'C4':
        	if dest[2] == '0':
                    	path4 = '6'
        	else:
                    	path4 = '7'

    return path4


def main():

    inputs = []
    n = int(input("enter number of inputs:"))
    for i in range(n):
       randNum = random.randint(0, 7)
       while randNum in inputs:
		        randNum = random.randint(0, 7)
       inputs.append(randNum)
    print(inputs)
    inputs.sort()
    input_dict = {}
    i = 0
    while i < n:
        input_dict[i] = inputs[i]
        i += 1
        
    print("Randomly generated numbers for each port are", input_dict)

    starting_points = {'0': 'A1', '1': 'A2', '2': 'A3', '3': 'A4', '4': 'A1', '5': 'A2', '6': 'A3', '7': 'A4'}

    for i in range(n):
	        x = bin(input_dict[i])[2:].zfill(3)
	        Path1 = starting_points[str(i)]
	        Path2 = switchAtoB(Path1, x)
	        Path3 = switchBtoC(Path2, x)
	        Path4 = switchCtoOutput(Path3, x)
    print('Path from input port'+str(i)+ 'to output port' + str(input_dict[i])+'is'+''+ Path1 + '->' + Path2 + '->' + Path3 + '->'+ Path4)

main()