"""
	max product of substing
"""
import sys
def maxProdSub(aList):
	if not aList:
		return -sys.maxint-1

	maxEnd = aList[0]
	minEnd = aList[0]
	maxRes = aList[0]

	for i in range(1,len(aList)):
		end1 = aList[i] * maxEnd
		end2 = aList[i] * minEnd

		maxEnd = max(max(end1,end2), aList[i])
 		minEnd = min(min(end1,end2), aList[i])
 		maxRes = max(maxEnd, maxRes)


 	return maxRes
aList = []
print maxProdSub(aList)
aList = [1,2,3,-.3,0,0.3]
print maxProdSub(aList)