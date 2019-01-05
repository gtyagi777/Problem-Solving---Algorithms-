def findPlatform(arr,dep,n): 

	# Sort arrival and 
	# departure arrays 
	arr.sort() 
	dep.sort() 

	# plat_needed indicates 
	# number of platforms 
	# needed at a time 
	plat_needed = 1
	result = 1
	i = 1
	j = 0

	# Similar to merge in 
	# merge sort to process 
	# all events in sorted order 
	while (i < n and j < n): 
	
		# If next event in sorted 
		# order is arrival, 
		# increment count of 
		# platforms needed 
		if (arr[i] < dep[j]): 
		
			plat_needed+=1
			i+=1

			# Update result if needed 
			if (plat_needed > result): 
				result = plat_needed 
		

		# Else decrement count 
		# of platforms needed 
		else: 
		
			plat_needed-=1
			j+=1
		
	return result 

# driver code 

arr=[1,2,6,5,3]
dep=[5,5,7,6,8]
n = len(arr) 

print("Minimum Number of Platforms Required = ", 
		findPlatform(arr, dep, n)) 

# This code is contributed 
# by Anant Agarwal. 
