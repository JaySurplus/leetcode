"""
	There are N children standing in a line. Each child is assigned a rating value.

	You are giving candies to these children subjected to the following requirements:

		Each child must have at least one candy.
		Children with a higher rating get more candies than their neighbors.
	What is the minimum candies you must give?
"""

class Solution(object):
	def candyII(self, ratings):
		"""
		:type ratings: List[int]
		:rtype: int
		"""
		res = [1 for i in range(len(ratings))]
		
		for i in range(1, len(ratings)):
			if ratings[i] > ratings[i-1]:
				res[i] = res[i-1]+1

		
		for i in range(len(ratings)-2, -1,-1):
			if ratings[i+1] < ratings[i] and res[i+1] >= res[i]:
				res[i] = res[i+1] + 1


		return sum(res)

	def candy(self, ratings):

		cands = 1
		cands_at_last_peak = 1
		debt = 0
		for i in xrange(1, len(ratings)):
			if ratings[i] < ratings[i-1]:
				debt += 1
				continue
			
			if debt > 0:
				cands += max((debt+2)*(debt+1)/2-cands_at_last_peak, (debt+1)*debt/2)
				debt = 0
				cands_at_last_peak = 1
			cands_at_last_peak = 1 if ratings[i] == ratings[i-1] else cands_at_last_peak + 1
			cands += cands_at_last_peak
		if debt > 0:
			cands += max((debt+2)*(debt+1)/2-cands_at_last_peak, (debt+1)*debt/2)
		return cands

	def candyIII(self, ratings):
		cands = 1
		last_peak = 1
		debet = 0

		for i in range(1, len(ratings)):
			if ratings[i] < ratings[i-1]:
				debet += 1
				continue

			if debet > 0:
				cands += max( (debet+1) * (debet+2)/2 - last_peak , debet * (debet+1) /2 )
				debet = 0
				last_peak = 1

			last_peak = 1 if ratings[i] == ratings[i-1] else last_peak + 1
			cands += last_peak

		if debet > 0:
			cands += max( (debet+1) * (debet+2)/2 - last_peak , debet * (debet+1) /2 )

		return cands



sol = Solution()
ratings = [1,1,1,1,1,3,4,61,3,4,52,3,1,1,3,5,7,2,1,3,5,7]
#ratings = [1,1,1,1,1,4]
res = sol.candyIII(ratings)
print res