"""
	110. Balanced Binary Tree

	Given a binary tree, determine if it is height-balanced.

	For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import math
class Solution(object):
    def isBalancedII(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def depth(root , isTrue):
        	if not root:
        		return (0 , True)
        	if not isTrue:
        		return (-2,False)

        	l = depth(root.left,isTrue)
        	r = depth(root.right,isTrue)

        	if not (l[1] or r[1]):
        		return (-2,False)
        	if math.fabs(l[0]-r[0]) > 1:
        		return (-2,False)
        	return (max(l[0],r[0])+1, True)
        	
        if not root:
        	return True

        return depth(root , True)[1]

    def isBalanced(self, root):
    	def depth(root):
    		if not root:
    			return 0
    		return max(depth(root.left),depth(root.right)) + 1

    	if not root:
    		return True

    	diff = depth(root.left) - depth(root.right)
    	if diff < -1 or diff >1:
    		return False
    	return self.isBalanced(root.left) and self.isBalanced(root.right)


n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)

n1.left = n2
n2.left = n3

n1.right = n4
n4.left = n5

sol = Solution()
print sol.isBalancedII(n1)