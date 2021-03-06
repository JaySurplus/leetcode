"""
    414. Third Maximum Number
    Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

    Example 1:
        Input: [3, 2, 1]

        Output: 1

        Explanation: The third maximum is 1.
    Example 2:
        Input: [1, 2]

        Output: 2

        Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
    Example 3:
        Input: [2, 2, 3, 1]

        Output: 1

        Explanation: Note that the third maximum here means the third maximum distinct number.
    Both numbers with value 2 are both considered as second maximum.
"""
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        uniq = list(set(nums))
        if len(uniq) < 3:
            return max(uniq)
        if len(uniq) == 3:
            return min(uniq)
        a, b, c = uniq[:3]
        ma = max(a,b,c)
        mi = min(a,b,c)
        mid = sum(uniq[:3]) - ma - mi
        for i in range(3, len(uniq)):
            if uniq[i] > ma:
                ma = uniq[i]
            elif uniq[i] > mid:
                mi = mid
                mid = uniq[i]
            elif uniq[i] > mi:
                mi = uniq[i]
        return mi

