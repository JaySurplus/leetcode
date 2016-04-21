class Solution(object):
    def countPrimes(self, n):
    	marked = 0
    	count = 0
    	curr = 0
    	last = 0
    	l = [0 for i in range(n-1)]
    	while marked < n-1:
   
        	for i in range(last, n-1):
        		if l[i] == 0:
        			l[i] = 1
        			last = i+1
        			count += 1
        			marked += 1
        			break
        	
        	base = i + 2
        	t = 2
        	while base*t <= n:
        		if l[base*t-2] == 0:
        			l[base*t-2] = 1
        			marked += 1
        		t += 1
        	
        return count

    def countPrimesII(self, n):
    	if n <= 2:
    		return 0
    	if n == 3:
    		return 1

    	ls = [True] * (n-1)

    	
    	
    	count = 1
    	
    	for i in xrange(3,int((n-1)**0.5+1) , 2 ):
    		if ls[i-1]:
    			for j in xrange(i*i,n, i*2):
    				ls[j-1] = False
    	
    	for i in xrange(3,n, 2):
    		if ls[i-1]:
    			count += 1
   
    	return count



sol = Solution()
print sol.countPrimesII(97)