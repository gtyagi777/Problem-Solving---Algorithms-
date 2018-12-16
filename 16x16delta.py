# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 19:31:33 2018

@author: tyagi
"""

def banyan(x):
    inpBan= {}
    series = []
    for i in range(len(x)):
        inpBan[i] = x[i]
        series.append(x[i])
        
        
    path1 = {
    	 'a1' : [ 'b1', 'b5'],
        'a2' : [ 'b2', 'b6'],
        'a3' : [ 'b3', 'b7'],
        'a4' : [ 'b4', 'b8'],
        'a5' : [ 'b1', 'b5'],
        'a6' : [ 'b2', 'b6'],
        'a7' : [ 'b3', 'b7'],
        'a8' : [ 'b4', 'b8'],

    }
    
    path2 = {
    	  'b1' : [ 'c1', 'c3'],
        'b2' : [ 'c2', 'c4'],
        'b3' : [ 'c1', 'c3'],
        'b4' : [ 'c2', 'c4'],
        'b5' : [ 'c5', 'c7'],
        'b6' : [ 'c6', 'c8'],
        'b7' : [ 'c5', 'c7'],
        'b8' : [ 'c6', 'c8'],

    }
    
    path3 = {
    	 'c1' : [ 'd1', 'd2'],
        'c2' : [ 'd1', 'd2'],
        'c3' : [ 'd3', 'd4'],
        'c4' : [ 'd3', 'd4'],
        'c5' : [ 'd5', 'd6'],
        'c6' : [ 'd5', 'd6'],
        'c7' : [ 'd7', 'd8'],
        'c8' : [ 'd7', 'd8'],
    }
    
    path4= {
            'd1' : [ 'out0', 'out1'],
            'd2' : [ 'out2', 'out3'],
            'd3' : [ 'out4', 'out5'],
            'd4' : [ 'out6', 'out7'],
            'd5' : [ 'out8', 'out9'],
            'd6' : [ 'out10', 'out11'],
            'd7' : [ 'out12', 'out13'],
            'd8' : [ 'out14', 'out15'],

    	}
    
    Inputpath= {
            0:'a1',
            1:'a1',
            2:'a2',
            3:'a2',
            4:'a3',
            5:'a3',
            6:'a4',
            7:'a4',
            8:'a5',
            9:'a5',
            10:'a6',
            11:'a6',
            12:'a7',
            13:'a7',
            14:'a8',
            15:'a8',
            
    	}
    
    def e2epath(current_nod, user_input1):
    	if user_input1 == '0':
    		node = current_nod[0]
    		print( 'bit => 0 : ' + node)
    		return node
    	else:
    		node = current_nod[1]
    		print('bit => 1 : ' + node)
    		return node    
        
    for i in range(len(x)):
        u_input = inpBan[i]
        p = "{0:b}".format(u_input)
        if len(p) == 2:
            p = '00'+ p
        elif len(p) == 1:
             p = '000'+ p
        elif len(p) == 3:
             p = '0'+ p
        u_input = list(p)
        print('\n'+'Desired output is ' + str(u_input))
        print("Starting from : " + Inputpath[i])
        node1 = e2epath(path1[Inputpath[i]], u_input[0])
        node2 = e2epath(path2[node1], u_input[1])
        node3 = e2epath(path3[node2], u_input[2])
        node4 = e2epath(path4[node3], u_input[3])
        print(Inputpath[i], " ->" ,node1, " -> " ,node2, " -> " ,node3, " -> " ,node4 )

def batcher(x):
    def merge(a,b):
        """ Function to merge two arrays """
        c = []
        while len(a) != 0 and len(b) != 0:
            if a[0] < b[0]:
                c.append(a[0])
                a.remove(a[0])
            else:
                c.append(b[0])
                b.remove(b[0])
        if len(a) == 0:
            c += b
        else:
            c += a
        return c
    
    def mergesort(x):
        """ Function to sort an array using merge sort algorithm """
        if len(x) == 0 or len(x) == 1:
            return x
        else:
            middle = len(x)//2
            a = mergesort(x[:middle])
            b = mergesort(x[middle:])
            return merge(a,b)
    
    x = mergesort(x)
    return x

def randomize(x):
    import random
    random.shuffle(x)
    return x

def input_func():
    #OUTPUT port sequence
    inp = [12,15]
    inp = randomize(inp)

    print("input sequence to Batcher : ", inp)
    inp = batcher(inp)
    print(inp)
    banyan(inp)

input_func()
        
        
        
        

