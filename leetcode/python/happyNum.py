class Solution:
    # @param {integer} n
    # @return {boolean}
    def squareByDigit(self, n):
    	if n <= 1:
    		return n
    	return (n%10)**2 + self.squareByDigit(n/10)
    

    def isHappy(self, n):
        numList = {}
        while n is not 1 and n not in numList.keys():
        	numList[n] = 0
        	n = self.squareByDigit(n)

        if n in numList.keys():
        	return False
        return True
        


n = 100
test = Solution()
print test.squareByDigit(n)

aList =[]
r = 50000
for i in range(r):
	if test.isHappy(i+1):
		aList.append(i+1)
		#print i+1
print 'From 1 to %d, there are %d happy numbers'%(r, len(aList))