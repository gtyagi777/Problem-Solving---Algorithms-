<<<<<<< HEAD
def sumBitDifferences(arr,n): 
  
    ans = 0  # Initialize result 
  
    # traverse over all bits 
    for i in range(0, 32): 
      
        # count number of elements with i'th bit set 
        count = 0
        for j in range(0,n): 
            x = arr[j]
            y = 1 << i
            z = x & y
            if ( z ): 
                count+=1
  
        # Add "count * (n - count) * 2" to the answer 
        ans += (count * (n - count) * 2); 
      
    return ans 
  
# Driver prorgram 
arr = [1, 3, 5] 
n = len(arr ) 
=======
def sumBitDifferences(arr,n): 
  
    ans = 0  # Initialize result 
  
    # traverse over all bits 
    for i in range(0, 32): 
      
        # count number of elements with i'th bit set 
        count = 0
        for j in range(0,n): 
            x = arr[j]
            y = 1 << i
            z = x & y
            if ( z ): 
                count+=1
  
        # Add "count * (n - count) * 2" to the answer 
        ans += (count * (n - count) * 2); 
      
    return ans 
  
# Driver prorgram 
arr = [1, 3, 5] 
n = len(arr ) 
>>>>>>> 34dcdbaf7606329ea73cdb976296a4aeaa79cb79
print(sumBitDifferences(arr, n)) 