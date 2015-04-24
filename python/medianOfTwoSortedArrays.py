class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def getK(self, listA, listB, k , even = False):
    	lenA = len(listA)
    	lenB = len(listB)
        if lenA > lenB:
            return self.getK(listB, listA , k , even)
    	if lenA == 0:
    		return self.lengthIsZero(listB, k , even)

    	if k == 1:
            if even:
                a=listA[0]
                b=listB[0]
                if a <= b:
                    return  1.0*(a +self.getK(listA[1:] , listB , 1, False))/2
                return 1.0*(a + self.getK(listA, listB[1:] , 1, False))/2
            return min(listA[0], listB[0])


    def lengthIsZero(self, alist , k ,even):
    	
    	if even:
    		return 1.0 * (alist[k-1] + alist[k])/2 
    	return alist[k-1]


    def findMedianSortedArrays(self, nums1, nums2):
        length = len(nums1) + len(nums2)
        k = 1 + length / 2
        if length%2 == 0:
        	return self.getK(listA,listB,k, True)
        return self.getK(listA,listB,k ,False)


a = [1,4,4,4,5,6]
b = [3,7,12,17,19]

test = Solution()
print test.lengthIsZero(a, 4, False)
print test.getK(a,b,1,True)