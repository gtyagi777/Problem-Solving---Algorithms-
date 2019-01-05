# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 20:56:10 2018

@author: tyagi
"""

def returnPalindrome(strng):
    x = len(strng)//2
    if len(strng)%2 !=0:
        if strng >= strng[:x+1]+ strng[:x][::-1]:
            number = int(strng[:x+1])
            number += 1
            number = str(number)
            number = number + number[::-1][1:]
            return number
        else:
            return strng[:x+1]+ strng[:x][::-1]
                   
    else:
        if strng > strng[:x]+ strng[:x][::-1]:
            number = int(strng[:x])
            number += 1
            number = str(number)
            number = number + number[::-1]
            return number
        else:
            return strng[:x]+ strng[:x][::-1]
        
def generateNextPalindromeUtil(num) : 
    num = list(map(int,num))
    xx = set(num)
    if len(xx) == 1 and 9 in xx:
        return int("".join(map(str,num)))+ 2
    n = len(num)
    mid = n//2 
    leftsmaller = False
    i = mid - 1
    j = mid + 1 if (n % 2) else mid  
    while (i >= 0 and num[i] == num[j]) : 
        i-=1
        j+=1

    if ( i < 0 or num[i] < num[j]):  
        leftsmaller = True
  
    while (i >= 0) : 
      
        num[j] = num[i]  
        j+=1
        i-=1

    if (leftsmaller == True) : 
      
        carry = 1
        i = mid - 1

        if (n%2 == 1) : 
          
            num[mid] += carry  
            carry = int(num[mid] // 10 ) 
            num[mid] %= 10
            j = mid + 1
          
        else: 
            j = mid  
  
  
        while (i >= 0) : 
          
            num[i] += carry  
            carry = num[i] // 10
            num[i] %= 10
            num[j] = num[i] # copy mirror to right 
            j+=1
            i-=1
    
    return "".join(map(str,num))

"""
#driver Program
for _ in range(int(input())):
    print(returnPalindrome(input()))
"""
   
##Test Program
print(generateNextPalindromeUtil("999"))


#driver Program
for _ in range(int(input())):
    print(generateNextPalindromeUtil(input()))
    
    