class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        test = (2**31)/10
        neg = False
		


        if x < 0 :
        	neg = True
        	x = -x

        result = 0
        while x != 0:
        	if result > 214748364:
        		result = 0
        		break
        	result = result*10 + x%10
        	x/=10
        	

        #if result > 2**31:
        #	return 0

        if neg:
        	return -result		
        return result



print 2**31
print 1000000003

test = Solution()
print test.reverse(123)
print test.reverse(-123)
print test.reverse(1534236469)
print 2**31
print test.reverse(1463847412)


