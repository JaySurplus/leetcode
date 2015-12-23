"""
	4Sum
	Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.
	https://leetcode.com/problems/4sum/
"""
import copy
import time
class Solution(object):




	def nSum(self, nums, target , start , end ,  n  ,finalResult , subResult):
		if n < 1 or n > end -start:
			return finalResult

		elif n == 1:
			# If n == 1, then return the first occurence of target.
			if nums[start] <= target and nums[end-1] >= target:
				for i in range(start, end):
				
					if nums[i] == target:

						subResult.append(nums[i]) 
						finalResult.append(subResult)
						return finalResult

		elif n == end - start :
			# if number of elements equals to n , then just check wether summation of nums is equals to target or not.
			if reduce(lambda x , y : x+y , nums[start:end]) == target:
				finalResult.append(nums[start:end])
			return finalResult


		elif n == 2:
			i = start
			j = end -1
			
			while i < j :

				if nums[i] == target - nums[j]:

					subResult.append(nums[i]) 
					subResult.append(nums[j])
					finalResult.append(subResult) 
					subResult = subResult[:-2]

					i+=1
					j-=1
				# skip redundant elements
					while i<j and nums[i] == nums[i-1]:
						i +=1 
							
					while i<j and nums[j] == nums[j+1] :
						j -= 1
						 

				elif nums[i] < target - nums[j]:
					i += 1
					while i<j and nums[i] == nums[i-1]:
						i +=1 
						
					
				else:
					j -= 1
					while i<j and nums[j] == nums[j+1]:
						j -= 1
				# skip down
					
		else:
			
			for i in range(start , end-n+1):
				# skip.
				if i+n <end : 
					if nums[i] != nums[i+n]:
						temp = copy.deepcopy(subResult)
						temp.append(nums[i]) 
						self.nSum(nums, target-nums[i] , i+1 , end, n-1 , finalResult, temp)

		return finalResult

	def fourSum(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[List[int]]
		"""
		nums.sort()
		finalResult = []
		subResult = []
		
		return self.nSum(nums, target , 0 , len(nums),4, finalResult, subResult)

    



sol = Solution()

#arr = [-491,-477,-450,-436,-431,-410,-402,-402,-391,-381,-380,-377,-355,-346,-344,-325,-320,-318,-290,-286,-278,-278,-272,-261,-261,-259,-235,-234,-232,-220,-212,-206,-201,-196,-191,-186,-173,-164,-158,-133,-120,-98,-91,-87,-82,-73,-62,-55,-27,0,14,19,23,37,48,52,53,53,57,83,85,106,161,170,174,183,188,191,197,211,212,222,231,243,250,274,284,302,313,319,332,338,356,358,369,374,396,406,416,420,425,440,441,443,469,471,496]
#arr = [-494,-474,-425,-424,-391,-371,-365,-351,-345,-304,-292,-289,-283,-256,-236,-236,-236,-226,-225,-223,-217,-185,-174,-163,-157,-148,-145,-130,-103,-84,-71,-67,-55,-16,-13,-11,1,19,28,28,43,48,49,53,78,79,91,99,115,122,132,154,176,180,185,185,206,207,272,274,316,321,327,327,346,380,386,391,400,404,424,432,440,463,465,466,475,486,492]
arr = [-1,1,0,0,-2,2]
#arr = [-491,-468,-450,-415,-414,-374,-357,-333,-305,-292,-274,-272,-271,-258,-241,-240,-227,-217,-196,-184,-161,-120,-116,-110,-110,-98,-92,-47,-27,-10,-8,-7,-4,-1,19,30,53,62,64,65,137,138,145,160,178,179,209,221,243,270,279,283,290,291,305,308,322,345,354,357,365,366,368,371,376,381,381,394,400,406,429,433,445,446,449,470,471,472]
#arr = [1,1,1,1,1,1,1,1,1,1,2]
#target =2873
#target = -1201
target = 0
start = time.time()
result = sol.fourSum(arr , target)
end = time.time()
print result
print end - start
