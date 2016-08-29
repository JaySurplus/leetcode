"""
    306 Additive Number
    https://leetcode.com/problems/additive-number/
"""

class Solution(object):
    def isAdditiveNumberII(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        for i in xrange(1,n/2+1):
            for j in xrange(i+1,n):
                a = num[:i]
                if a != str(int(a)):
                    return False
                b = num[i:j]
                if b != str(int(b)):
                    break

                if max(len(a),len(b)) > n - len(a) - len(b):
                    break
                c = str(int(a)+int(b))
                while j + len(c) < n and c == num[j:j+len(c)]:
                    a = b
                    b = c
                    j += len(c)
                    c = str(int(a)+int(b))
                if j + len(c) == n and c == num[j:j+len(c)]:
                    return True
        return False


    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        if len(num) < 3:
            return False

        for i in range(1,len(num)/2+1):
            for j in range(i+1,len(num)):
                if j - i  > (len(num))/2:
                    break
                a = num[:i]
                b = num[i:j]
                c = str(int(a) + int(b))
                if self.helper(a,b,num[j:]):
                    return True

        return False

    def helper(self,a, b, c):
        if c == "":
            return True
        else:
            tempSum = str(int(a) + int(b))
            if len(tempSum) > len(c):
                return False
            else:
                if tempSum == c[:len(tempSum)] and c[0] != '0':
                    return self.helper(b,tempSum,c[len(tempSum):])
                return False

sol = Solution()
nums = "11235812"
nums = "11235813"
nums = "199100199"
print sol.isAdditiveNumber(nums)




