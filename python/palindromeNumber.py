"""
	Palindrome Number
	https://leetcode.com/problems/palindrome-number/
"""
#import math


class Solution(object):

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0:
            return False
        if x < 10:
            return True

        def size(n):
            size = 0
            while n / 10 != 0:
                size += 1
                n = n / 10
            return size

        size = size(x)

        if x % 10 != x / 10**size:
            return False
        else:
            x = x % 10**size
            x = x / 10
            return self.isPalindrome(x)

    def isPalindromeII(self, x):
        if x < 0:
            return False
        if x < 10:
            return True
        if x % 10 == 0:
            return False
        y = 0
        while x > y:
            y = y * 10 + x % 10
            x = x / 10

        return x == y / 10 or x == y

        '''
        #print size
        while size >= 1:
        	#print x%10 , x/(10**size)
        	if x%10 != x/(10**size):
        		return False
        	x = (x/10)%(10**(size-1))
        	size -= 2 
        	#print size
        return True
        '''
        """
        if x < 0:
        	return False
        if x < 10:
        	return True
        result = 0
        size = 0
        rand = 0
        size = int(math.log(x,10))
       
        rand = (size+1)/2
        while rand > 0:
			result = result*10 + x%10
			rand -=1
			x /= 10

        if size %2 == 0:
        	x /=10

        	#if result > 2147487412: #214747412
        print result
        print x
        return result == x	
        """


def main():
    test = Solution()
    # return test.isPalindrome(1)
    print test.isPalindromeII(112211)
    print test.isPalindromeII(1123211)
    print test.isPalindromeII(112321411)
    print test.isPalindromeII(11211)

if __name__ == '__main__':
    main()
