<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 18:52:03 2018

@author: tyagi
"""

def countLeaves(root):
    # Code here
    if root == None:
        return 0
    
    count = 0
    x = []
    x.append(root)
    while len(x)!= 0:
        z = x.pop()
        if z.left == None and z.right == None:
            count += 1
        else:
            if z.left != None:
                x.append(z.left)
            if z.right != None:
                x.append(z.right)
    
=======
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 18:52:03 2018

@author: tyagi
"""

def countLeaves(root):
    # Code here
    if root == None:
        return 0
    
    count = 0
    x = []
    x.append(root)
    while len(x)!= 0:
        z = x.pop()
        if z.left == None and z.right == None:
            count += 1
        else:
            if z.left != None:
                x.append(z.left)
            if z.right != None:
                x.append(z.right)
    
>>>>>>> 34dcdbaf7606329ea73cdb976296a4aeaa79cb79
    return count