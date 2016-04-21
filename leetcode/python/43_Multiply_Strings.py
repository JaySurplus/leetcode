"""
	43. Multiply Strings 

	Total Accepted: 49572 Total Submissions: 223667 Difficulty: Medium

	Given two numbers represented as strings, return multiplication of the numbers as a string.

	Note: The numbers can be arbitrarily large and are non-negative.

	https://leetcode.com/problems/multiply-strings/
"""

import time


class Solution(object):
    def multiply(self, num1, num2):
    	num1 = num1[::-1]
    	num2 = num2[::-1]
    	arr = [ 0 for i in range(len(num1)+ len(num2))]
    	for i in range(len(num1)):		
    		for j in range(len(num2)):
    			arr[i+j] += int(num1[i]) * int(num2[j])
   

    	result = []
    	for i in range(len(arr)):
    		digit = arr[i] % 10
    		carry = arr[i] / 10
    		if i < len(arr) -1 :
    			arr[i+1] += carry
    		result.insert( 0,str(digit))

    	while result[0] == '0' and len(result) > 1:
    		del result[0]

    	return ''.join(result)
    	"""
        if num1 == '0' or num2 =='0':
        	return '0'

       	
        nums1 = num1[::-1]
        nums2 = num2[::-1]

        result = []
        
        for i in range(len(nums1)):
        	temp = []
        	n = 0
        	for j in range(len(nums2)):
        
        		prod = int(nums1[i]) * int(nums2[j])
        		temp.append( (prod+n)%10)
        		n = (prod+n)/10
        	if n != 0:
        		temp.append(n)
        	result.append(temp)
        
        f = result[0]
        for i in range(1,len(result)):
        	
        	f = self.add(f,result[i],i)
        	

        
        f = reduce( lambda x , y : str(x)+str(y) , f,'')[::-1]
        return f

    def add(self , x , y , i):
		
		n = 0
		k = i
		while k < len(x):
			v = x[k] + y[k-i] + n
			x[k] = v%10
			n = v/10
			k+=1
	
		while k - i< len(y):
			v = y[k-i] + n
			x.append(v%10)
			n = v/10
			k+=1
	
		if n != 0:
			x.append(n)

		return x
	"""







sol = Solution()
num1 = "141235126346235132412412412351212431241241254312515162624245356123464513451241241234123412412346245431206412469231651205631256129"
num2 = "43127459012571275017123511264513313412412412412412545641241241514890614128942451289467126451256217861289467123846128457125093431274591284571516"

start1 = time.time()
result =sol.multiply(num1,num2)
end1 = time.time()

start2 = time.time()
result2 = int(num1) * int(num2)
end2 = time.time()

print end1 - start1
print result

print

print end2 - start2
print result2