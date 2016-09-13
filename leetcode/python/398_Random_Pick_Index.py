"""
    398 Random Pick Index

    Given an array of integers with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.

    Note:
    The array size can be very large. Solution that uses too much extra space will not pass the judge.

    Example:

        int[] nums = new int[] {1,2,3,3,3};
        Solution solution = new Solution(nums);

        // pick(3) should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
        solution.pick(3);

        // pick(1) should return 0. Since in the array only nums[0] is equal to 1.
        solution.pick(1);
"""
from collections import defaultdict
import random
class Solution(object):

    def __init__(self, nums):

        """
        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums


    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        count = 0
        res = 0
        for i in range(len(self.nums)):
            if self.nums[i] == target:
                if random.randint(0,count) == 0:
                    res = i
                count += 1
        return res


#Your solution object will be instantiated and called as such:
#obj = Solution(nums)
#param_1 = obj.pick(target)

if __name__ == '__main__':
    nums = [1,2,3,3,3,3,3,3,3,3,3,3]
    sol = Solution(nums)
    dic = {}
    for i in range(10000):
        res = sol.pick(3)
        if res not in dic:
            dic[res] = 0
        dic[res] += 1
    print dic
    for key in dic:
        print "value %d: %f " % (key, 1.*dic[key]/10000)


