"""
	85. Maximal Rectangle

	Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing all ones and return its area.


	https://leetcode.com/problems/maximal-rectangle/
"""
import random
class Solution(object):
	"""
	def largestRectangleArea(self, height):
		stack=[]; i=0; area=0
		while i<len(height):
			if stack==[] or height[i]>height[stack[len(stack)-1]]:
				stack.append(i)
			else:
				curr=stack.pop()
				width=i if stack==[] else i-stack[len(stack)-1]-1
				area=max(area,width*height[curr])
				i-=1
			i+=1
		while stack!=[]:
			curr=stack.pop()
			width=i if stack==[] else len(height)-stack[len(stack)-1]-1
			area=max(area,width*height[curr])
		return area
	def maximalRectangle(self, matrix):
		if matrix==[]: return 0
		a=[0 for i in range(len(matrix[0]))]; maxArea=0
		for i in range(len(matrix)):
			for j in range(len(matrix[i])):
				a[j]=a[j]+1 if matrix[i][j]=='1' else 0
			maxArea=max(maxArea, self.largestRectangleArea(a))
		return maxArea
	"""
	def maximalRectangle(self, matrix):
		if len(matrix) == 0 or len(matrix[0]) == 0:
			return 0
		m = len(matrix)
		n = len(matrix[0])
		res = 0

		for i in range(m):
			for j in range(n):
				if matrix[i][j] == '1':
					a, b,l, r ,c= self.dfs(matrix, i ,j,0)

					if c > res:
						tempRes = self.help([line[l:r+1] for line in matrix[a:b+1]])
						res = max(res,tempRes)
		
		return res

	def dfs(self,matrix , i , j ,count):
		matrix[i][j] = 'V'
		count += 1
		a , b , l , r = i , i , j , j
		
		
		
		if (i > 0  and matrix[i-1][j] == '1'):
			(at,bt,lt,rt,c) = self.dfs(matrix, i-1 ,j,count)
			a -= 1
			a = min(a,at)
			b = max(b,bt)
			l = min(l,lt)
			r = max(r,rt)
			count = c
			
		


		if ( i < len(matrix)-1 and matrix[i+1][j]=='1'):
			(at,bt,lt,rt,c) = self.dfs(matrix, i+1,j,count)
			a = min(a,at)
			b = max(i+1,bt)
			l = min(l,lt)
			r = max(r,rt)
			count = c
			
		

		if (j>0  and matrix[i][j-1] == '1'):
			(at,bt,lt,rt,c) = self.dfs(matrix,i,j-1,count)
			a = min(a,at)
			b = max(b,bt)
			l = min(j-1,lt)
			r = max(r,rt)
			count = c
			


		if (j<len(matrix[0])-1 and matrix[i][j+1]=='1'):
			(at,bt,lt,rt,c) = self.dfs(matrix , i ,j+1,count)
			a = min(a,at)
			b = max(b,bt)
			l = min(l,lt)
			r = max(j+1,rt)
			count = c
			


		return (a,b,l,r,count)

	def help(self, matrix):

		
		if len(matrix) == 0 or len(matrix[0]) == 0:
			return 0
		m = len(matrix)
		n = len(matrix[0])      
		above = 0
		below = 0
		right = 0
		left = 0
		for i in range(m):
			for j in range(n):
				if matrix[i][j] == "0":
					if i > 0:
						above = self.help(matrix[0:i])
					if i < m-1:
						below = self.help(matrix[i+1:])
					if j > 0:
						left = self.help([k[:j] for k in matrix])
					if j < n - 1:
						right = self.help([k[j+1:] for k in matrix])
					return reduce(lambda x, y: max(x,y) , [above, below, left,right])
		return m*n			
	
def matrix(m ,n ,k):
	rand = random.sample(range(m*n) , k)
	matrix = [ [ str(0) for i in range(n)] for j in range(m)]
	
	for i in range(m):
		for j in range(n):
			if i*n+j in rand:
				matrix[i][j] = "1"
	return matrix



sol = Solution()


m = matrix(100,1000,10000)

for i in m:
	print ' '.join(i)
print 

print sol.maximalRectangle(m)
print 
"""
for i in m:
	print ''.join(i)
"""