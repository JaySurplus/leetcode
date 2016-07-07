"""
    270. Closest Binary Search Tree Value
    Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

    Note:
    Given target value is a floating point.
    You are guaranteed to have only one unique value in the BST that is closest to the target.

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        if not root.left and not root.right or root.val == target:
            return root.val

        res = root.val

        while root:
            if root.val == target:
                return root.val

            res = root.val if  abs(root.val - target) < abs(res - target) else res

            if root.val > target:
                root = root.left
            else:
                root = root.right
        return res

    def closestValueII(self, root, target):
        a = root.val
        if target == a:
            return a
        if target < a:
            kid = root.left
        else:
            kid = root.right
        if not kid:
            return a
        b = self.closestValue(kid, target)
        return min((b, a), key=lambda x: abs(target - x))


