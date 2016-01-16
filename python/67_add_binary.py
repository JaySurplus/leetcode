"""
	67. Add Binary

	https://leetcode.com/problems/add-binary/

	Given two binary strings, return their sum (also a binary string).

	For example,
	a = "11"
	b = "1"
	Return "100".
"""

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        la = len(a)
        lb = len(b)

        if la >= lb:
        	l = a
        	s = b
        else:
        	l = b
        	s = a

        
        ll = [int(_) for _ in l]
        sl = [int(_) for _ in s]
      
        i = -1
        carry = 0
        while i >= -len(sl):
        	s = ll[i] + sl[i] + carry
        	ll[i] = s%2
        	carry = s/2
        	i -= 1
   
        if carry == 0:
        	
        	return ''.join(map(lambda x : str(x), ll))
        else:
        	while i >= -len(ll) and carry != 0:
        		s = ll[i] + carry
        		ll[i] = s%2
        		carry = s/2
        		i -= 1
        	if carry != 0:
        		ll = [1] + ll
        	return ''.join(map(lambda x : str(x), ll))

    def addBinaryII(self,a,b):
    	la = len(a)
        lb = len(b)

        i = 1
        j = 1
        res = ''
        carry = 0
        
      
  
        
        while i <= la or j <= lb or carry == 1:

        	if i <= la:
        		carry += int(a[-i])
        		i += 1
        	if j <= lb:
        		carry += int(b[-j])
        		j += 1

        	res = str(carry%2) + res
        	
        	carry /= 2
        	
   
 
        return res


        

sol = Solution()
a = "11"
b = "11111111"
print sol.addBinaryII(a,b)