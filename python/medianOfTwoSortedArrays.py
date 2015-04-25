import math
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
                return 1.0*(b + self.getK(listA, listB[1:] , 1, False))/2
            return min(listA[0], listB[0])
        parA = min(lenA,k/2)
        parB = k - parA
        if listA[parA-1] <= listB[parB-1]:
            return self.getK(listA[parA:] , listB , parB, even)
        return self.getK(listA, listB[parB:] ,parA , even)


    def lengthIsZero(self, alist , k ,even):
    	if even:
    		return 1.0 * (alist[k-1] + alist[k])/2 
    	return alist[k-1]


    def findMedianSortedArrays(self, nums1, nums2):
        length = len(nums1) + len(nums2)
        k = int(math.ceil(1. * length / 2))
        print 'k: ',k
        if length%2 == 0:
        	return self.getK(nums1,nums2,k, True)
        return self.getK(nums1,nums2,k ,False)


a = [1,2]
b = [1,2]

test = Solution()
#print test.lengthIsZero(a, 4, False)
#print test.getK(a,b,1,True)
print test.findMedianSortedArrays(a, b )


a = []
b = [1,2,3,4,5]
print test.findMedianSortedArrays(a, b)
