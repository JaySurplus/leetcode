"""
	60. Permutation Sequence


	The set [1,2,3,...,n] contains a total of n! unique permutations.

	By listing and labeling all of the permutations in order,
	We get the following sequence (ie, for n = 3):

	"123"
	"132"
	"213"
	"231"
	"312"
	"321"
	Given n and k, return the kth permutation sequence.
"""
import math
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        facs = {0:1 , 1:1 ,2:2 ,3:6 , 4 :24 ,5:120 , 6:720 , 7:5040, 8:40320 , 9:362880 }
    	l = [ str(i) for i in range(1, n+1)]
    	res = ''
    	fac = math.factorial(n)
    	while n > 0:
    		fac /= n
    		t = (k - 1)/fac
    		res+=l[t]
    		k -= fac*t
    		n -= 1
    		l.remove(l[t])
    	
    	return res





sol = Solution()
n = 3
k = 4
print sol.getPermutation(99, 1)