"""
    404 Sum of Left Leaves
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumOfLeftLeavesI(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.count = 0
        self.helper(root, False)
        return self.count
    def helper(self, root, isLeft):
        if not root.left and not root.right and isLeft:
            self.count += root.val
            return
        if root.right:
            self.helper(root.right, False)
        if root.left:
            self.helper(root.left, True)
        return

    def sumOfLeftLeaves(self, root):
        if not root:
            return 0

        res = 0
        stack = [root]
        while stack:
            curr = stack.pop()
            if curr.left:
                if not curr.left.left and not curr.left.right:
                    res += curr.left.val
                else:
                    stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
        return res

