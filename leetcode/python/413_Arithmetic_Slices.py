"""
    413. Arithmetic Slices
    A sequence of number is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

    For example, these are arithmetic sequence:

        1, 3, 5, 7, 9
        7, 7, 7, 7
        3, -1, -5, -9
    The following sequence is not arithmetic.

        1, 1, 2, 5, 7

    A zero-indexed array A consisting of N numbers is given. A slice of that array is any pair of integers (P, Q) such that 0 <= P < Q < N.

    A slice (P, Q) of array A is called arithmetic if the sequence:
    A[P], A[p + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that P + 1 < Q.

    The function should return the number of arithmetic slices in the array A.


    Example:

        A = [1, 2, 3, 4]

        return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself.
"""
class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 3:
            return 0
        i = 0
        res = 0
        while i < len(A) - 2:
            diff = A[i+1] - A[i]
            j = i + 2
            while j < len(A) and diff == A[j] - A[j-1]:
                j += 1
            if j - i >= 3:
                res += ( j - i - 1 ) * (j-i-2) /2
            i = j - 1
        return res

if __name__ == '__main__':
    A = [1,2,3,4,5,6]
    sol = Solution()
    res = sol.numberOfArithmeticSlices(A)
    print(res)





