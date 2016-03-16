"""
	134. Gas Station

	There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

	You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

	Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.
"""
class Solution(object):
	def canCompleteCircuitII(self, gas, cost):
		"""
		:type gas: List[int]
		:type cost: List[int]
		:rtype: int
		"""
		if sum(gas) < sum(cost):
			return -1

		
		step = 0
		count = 0
		index = 0
		next_st = 0
		forward = True
		
		while step < len(gas):
			if forward:
				count += gas[next_st]-cost[next_st]
				next_st+=1
			else:
				index -= 1
				count += gas[index] - cost[index]
				
			if count < 0:
				forward = False
			else:
				forward = True

			step += 1
	
		return (index)%len(gas)

	def canCompleteCircuit(self, gas, cost):
		#if sum(gas) < sum(cost):
		#	return -1

		n = len(gas)

		curr_sum = 0
		index = 0
		min_sum = 0

		for i in range(1,n+1):
			curr_sum += gas[i-1]-cost[i-1]
			if curr_sum < min_sum:
				index = i 
				min_sum = curr_sum

		return index if curr_sum >= 0 else -1

sol = Solution()
gas = [0,12,0,0]
cost = [3,4,2,1]

res = sol.canCompleteCircuit(gas, cost)
print res

