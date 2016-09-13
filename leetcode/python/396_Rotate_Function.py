"""
    396 Rotate Function.

    Given an array of integers A and let n to be its length.

    Assume Bk to be an array obtained by rotating the array Ak positions clock-wise, we define a "rotation function" F on A as follow:

        F(k) = 0 * Bk[0] + 1 * Bk[1] + ... + (n-1) * Bk[n-1].

        Calculate the maximum value of F(0), F(1), ..., F(n-1).
"""
class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        step = sum(A)
        res = 0
        for i in range(len(A)):
            res += i * A[i] 
        prev = res
        for i in range(len(A)-1):
            temp = prev + step - A[len(A)-1-i] * len(A)
            prev = temp
            res = max(res, temp)
        return res


if __name__ == '__main__':
    sol = Solution()
    A = [4,3,2,6]
    print "Test 1: ", sol.maxRotateFunction(A)



