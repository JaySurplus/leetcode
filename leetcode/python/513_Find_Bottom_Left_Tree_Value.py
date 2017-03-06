"""
    513. Find Bottom Left Tree Value
    https://leetcode.com/problems/find-bottom-left-tree-value/?tab=Description
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findBottomLeftValueII(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return None
        stack = [root]
        leftMost = root
        while stack:
            temp_stack = []
            tempLeftMost = None
            while stack:
                tempNode = stack.pop(0)
                if tempNode.left:
                    if not tempLeftMost:
                        tempLeftMost = tempNode.left
                    temp_stack.append(tempNode.left)
                if tempNode.right:
                    if not tempLeftMost:
                        tempLeftMost = tempNode.right
                    temp_stack.append(tempNode.right)
            stack = temp_stack
            if tempLeftMost:
                leftMost = tempLeftMost
        return leftMost.val

    def findBottomLeftValue(self, root):
        if not root:
            return None

        self.res = [1,root]

        def helper(level,node):
            if not node.left and not node.right:
                if level > self.res[0]:
                    self.res = [level, node]

            else:
                if node.left:
                    helper(level+1,node.left)
                if node.right:
                    helper(level+1, node.right)
            return
        helper(1,root)
        return self.res[1].val



N1 = TreeNode(1)
N2 = TreeNode(2)
N3 = TreeNode(3)
N4 = TreeNode(4)
N5 = TreeNode(5)
N6 = TreeNode(6)
N7 = TreeNode(7)

N1.left = N2
N1.right = N3
N2.left = N4
N3.left = N5
N5.left = N7
N3.right = N6

sol = Solution()
print sol.findBottomLeftValue(N1)
