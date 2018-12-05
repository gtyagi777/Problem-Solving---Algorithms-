def banyan(x):
    inpBan= {}
    for i in range(len(x)):
        inpBan[i] = x[i]
        
        
    path1 = {
    	'a1':['b1', 'b3'],
    	'a2':['b2', 'b4'],
    	'a3':['b1', 'b3'],
    	'a4':['b2', 'b4'],
    }
    
    path2 = {
    	'b1':['c1', 'c2'],
    	'b2':['c1', 'c2'],
    	'b3':['c3', 'c4'],
    	'b4':['c3', 'c4'],
    }
    
    path3 = {
    	'c1':['out0', 'out1'],
    	'c2':['out2', 'out3'],
    	'c3':['out4', 'out5'],
    	'c4':['out6', 'out7'],
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
    	}
    
    def e2epath(current_node, user_input):
    	if user_input == '0':
    		node = current_node[0]
    		print('bit => 0 : ' + node)
    		return node
    	else:
    		node = current_node[1]
    		print('bit => 1 : ' + node)
    		return node    
        
    for i in range(len(x)):
        u_input = inpBan[i]
        print('\nDesired output  port is ' + str(u_input))
        p = "{0:b}".format(u_input)
        if len(p) == 2:
            p = '0'+ p
        elif len(p) == 1:
             p = '00'+ p
        u_input = list(p )
        print("Starting from : " + Inputpath[i])
        node1 = e2epath(path1[Inputpath[i]], u_input[0])
        node2 = e2epath(path2[node1], u_input[1])
        node3 = e2epath(path3[node2], u_input[2])
        print(Inputpath[i], " ->" ,node1, " -> " ,node2, " -> " ,node3 )

def batcher(a):
    def bitonic_sort(up, x):
        if len(x) <= 1:
            return x
        else: 
            first = bitonic_sort(True, x[:len(x) // 2])
            second = bitonic_sort(False, x[len(x) // 2:])
            return bitonic_merge(up, first + second)
    
    def bitonic_merge(up, x): 
        # assume input x is bitonic, and sorted list is returned 
        if len(x) == 1:
            return x
        else:
            bitonic_compare(up, x)
            first = bitonic_merge(up, x[:len(x) // 2])
            second = bitonic_merge(up, x[len(x) // 2:])
            return first + second
    
    def bitonic_compare(up, x):
        dist = len(x) // 2
        for i in range(dist):  
            if (x[i] > x[i + dist]) == up:
                x[i], x[i + dist] = x[i + dist], x[i] #swap
    
    x = bitonic_sort(True,a)
    return x


def randomize(x):
    import random
    random.shuffle(x)
    return x

def input_func():
    #OUTPUT port sequence
    inp = [6]

    inp = randomize(inp)
    print("Randomized array :",inp)

    print("input sequence to Batcher : ", inp)
    inp = batcher(inp)
    print("Ouput sequence from Batcher : ",inp)
    banyan(inp)

input_func()
        
        
        
        

