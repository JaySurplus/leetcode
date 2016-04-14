"""
	50.Pow(x, n)
"""

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
        	return self.myPow(1./x,-n)

        elif n == 0:
        	return 1

        else:
        	res = self.myPow(x,n/2)
        	if n%2 == 0:
        		return res**2
        	else:
        		return res**2 * x

    def myPowIII(self, x , n):
        if n == 0:
            return 1
        if n < 0:
            x = 1./x
            n = -n
       
        res = 1
        while n != 0:
            if n % 2 == 1:
                res *= x
            x *= x
            n >>= 1
        return res


    def myPowII(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
     
        if n < 0:
            return self.myPow(1./x , -n)
            
        if n == 0:
            return 1
        
        if n == 1:
            return x
      
        else:
            
            p = 0
            while x % 2 == 0:
                x /= 2
                p += 1
            
            part = 1 << (n * p)
            res = 1

            while n != 0:
                if n % 2 == 1:
                    res *= x
                x *= x
                n >>= 1
            
            return part * res


import time
sol = Solution()
s1 = time.time()
res1=sol.myPowIII(128,432)
e1 = time.time()

s2 = time.time()
res2=sol.myPowII(128,432)
e2 = time.time()

print res1 == res2 

print "method III" ,e1-s1
print "method II ",e2-s2
