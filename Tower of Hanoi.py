<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 10:55:14 2018

@author: tyagi
"""

A = [5, 4,3, 2, 1]
B = []
C = []

def move(n, source, target, auxiliary):
    if n > 0:
        # move n - 1 disks from source to auxiliary, so they are out of the way
        move(n - 1, source, auxiliary, target)

        # move the nth disk from source to target
        target.append(source.pop())

        # Display our progress
        print(A, B, C, '##############', sep = '\n')

        # move the n - 1 disks that we left on auxiliary onto target
        move(n - 1, auxiliary, target, source)

# initiate call from source A to target C with auxiliary B
=======
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 10:55:14 2018

@author: tyagi
"""

A = [5, 4,3, 2, 1]
B = []
C = []

def move(n, source, target, auxiliary):
    if n > 0:
        # move n - 1 disks from source to auxiliary, so they are out of the way
        move(n - 1, source, auxiliary, target)

        # move the nth disk from source to target
        target.append(source.pop())

        # Display our progress
        print(A, B, C, '##############', sep = '\n')

        # move the n - 1 disks that we left on auxiliary onto target
        move(n - 1, auxiliary, target, source)

# initiate call from source A to target C with auxiliary B
>>>>>>> 34dcdbaf7606329ea73cdb976296a4aeaa79cb79
move(5, A, C, B)