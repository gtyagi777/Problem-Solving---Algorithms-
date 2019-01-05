def romanToInt(s):
        """
        :type s: str
        :rtype: int
        """
        r = {'I':1, 'V' : 5, 'X':10, 'L':50 , 'C':100,'D':500, 'M':1000}
        n = len(s)
        res = 0
        
        if s[-2:] == 'IV':
            res += 4
            n = n-2
        elif s[-2:] == 'IX':
            res += 9
            n = n-2
        i=0       
        while i < n :
            res += r[s[i]]
            i += 1
        return res

print(romanToInt("MCMXCIV"))