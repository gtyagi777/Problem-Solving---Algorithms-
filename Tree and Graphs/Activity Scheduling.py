# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 12:55:39 2018

@author: tyagi
"""

def printMaxActivities(s ): 
	n = len(s) 
	print ("The following activities are selected")

	# The first activity is always selected 
	i = 0
	print (s[i]) 

	# Consider rest of the activities 
	for j in range(n): 

		# If this activity has start time greater than 
		# or equal to the finish time of previously 
		# selected activity, then select it 
		if s[j][1] >= s[i][0]: 
			print (s[j])
			i = j 

# Driver program to test above function 
s = [1 , 3 , 0 , 5 , 8 , 5] 
f = [2 , 4 , 6 , 7 , 9 , 9] 

group = []

for i in range(len(s)) :
    group.append((f[i],s[i]))
    
printMaxActivities(group) 