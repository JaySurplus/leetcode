class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def getK(self, listA, listB, k , even = False):
    	lenA = len(listA)
    	lenB = len(listB)
    	if lenA == 0:
    		return self.lengthIsZero(listB, k , even )
    	if lenB == 0:
    		return self.lengthIsZero(listA, k , even )

    	if k == 1:
    		if even:
    			return 1.0 *(min(listA[0], listB[0]) + min(min(listA[0] , listB[1]) ,min(listA[1] , listB[0])) )/2
    		return min(listA[0], listB[0])


    def lengthIsZero(self, alist , k ,even):
    	
    	if even:
    		return 1.0 * (alist[k] + alist[k+1])/2 
    	return alist[k]


    def findMedianSortedArrays(self, nums1, nums2):
        length = len(nums1) + len(nums2)
        k = 1 + length / 2
        if length%2 == 0:
        	return self.getK(listA,listB,k, True)
        return self.getK(listA,listB,k ,False)


a = [1,2,3,4,5,6]
b = [2,7,12,17,19]

test = Solution()
#print test.lengthIsZero(a, 4, False)
print test.getK(a,b, 1  , True)