"""
	98. Validate Binary Search Tree

	Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.tree(root, -sys.maxint-1, sys.maxint)
    def tree(self, root , min , max):
    	if not root:
    		return True
    	if root.val <= min and root.val >= max:
    		return False
    	return self.tree(root.left , min, root.val) and self.tree(root.right , root.val , max )

sol = Solution()
