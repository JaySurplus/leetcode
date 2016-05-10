"""
    152. Maximum Product Subarray

    Find the contiguous subarray within an array (containing at least one number) which has the largest product.

    For example, given the array [2,3,-2,4],
    the contiguous subarray [2,3] has the largest product = 6.


"""
import unittest


class Solution(object):

    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        curr_min, curr_max = nums[0], nums[0]
        curr = nums[0]
        res = nums[0]
        for i in xrange(1, len(nums)):
            curr = curr_min
            curr_min = min(
                min(curr_min * nums[i], curr_max * nums[i]), nums[i])
            curr_max = max(max(curr * nums[i], curr_max * nums[i]), nums[i])
            res = max(res, curr_max)

        return res


class myTest(unittest.TestCase):

    def test(self):
        sol = Solution()
        nums = [2, 3, -2, 4]
        self.assertEqual(sol.maxProduct(nums), 6)

    def test2(self):
        sol = Solution()
        nums = [2, 3, -2, 4]
        self.assertEqual(sol.maxProduct(nums), 6)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(myTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
