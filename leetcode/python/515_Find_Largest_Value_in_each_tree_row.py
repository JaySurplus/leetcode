"""
    515. Find Largest Value in Each Tree Row
    https://leetcode.com/problems/find-largest-value-in-each-tree-row/?tab=Description
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return res
        stack = [root]
        res_temp = -2**31
        while stack:
            stack_temp = []
            while stack:
                temp = stack.pop(0)
                res_temp = max(res_temp, temp.val)
                if temp.left:
                    stack_temp.append(temp.left)
                if temp.right:
                   stack_temp.append(temp.right)
            res.append(res_temp)
            stack = stack_temp
            res_temp = -2**31
        return res

N1 = TreeNode(1)
N2 = TreeNode(3)
N3 = TreeNode(2)
N4 = TreeNode(5)
N5 = TreeNode(3)
N6 = TreeNode(9)

N1.left = N2
N1.right = N3
N2.left = N4
N2.right = N5
N3.right = N6


sol = Solution()
print sol.largestValues(N1)
