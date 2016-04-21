"""
	120. Triangle

	Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

	For example, given the following triangle
	[
    	 [2],
    	 [3,4],
   	     [6,5,7],
         [4,1,8,3]
	]

	[
		  [-1],
	      [3,2],
	    [-3,1,-1]]
	]
	The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
"""
class Solution(object):
	def minimumTotal(self, triangle):
		if len(triangle) == 0:
			return

		m_s = triangle[0][0]
		res = triangle[0]
		i = 1
		while i < len(triangle):

			triangle[i][0] =  res[0] + triangle[i][0] 
			m_s = triangle[i][0]
	
			

			l = len(triangle[i])
			for j in xrange(1,l-1):

				triangle[i][j]= min( triangle[i][j]+ res[j-1], res[j]+triangle[i][j])
				m_s = min(triangle[i][j] , m_s)
				
			
			triangle[i][l-1] = res[l-2] + triangle[i][l-1]
			m_s = min(triangle[i][l-1], m_s)
			res = triangle[i]
			i += 1
		return m_s


sol = Solution()
tri = [[2],[3,4],[6,5,7],[4,1,8,3]]
#tri = [[2], [2,3], [-4, -5 , -6]]
#tri = [[-1],[3,2],[-3,1,-1]]


for i in tri:
	print i



res = sol.minimumTotal(tri)
print res
