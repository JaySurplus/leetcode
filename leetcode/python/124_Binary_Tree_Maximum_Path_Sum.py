"""
	124. Binary Tree Maximum Path Sum

	Given a binary tree, find the maximum path sum.

	For this problem, a path is defined as any sequence of nodes from some 
	starting node to any node in the tree along the parent-child connections.
	The path does not need to go through the root.

	For example:
	Given the below binary tree,

       1
      / \
     2   3
	Return 6.
"""

class TreeNode(object):
	def __init__(self,x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def maxPathSum(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		self.currMax = float('-inf')
		self.helper(root)
		return self.currMax

	def helper(self, root):
		if not root:
			return root

		left = self.helper(root.left)
		right = self.helper(root.right)

		left = 0 if not left else (left if left > 0 else 0)
		right = 0 if not right else (right if right > 0 else 0)

		self.currMax = max(left + right + root.val , self.currMax)
		return max(left ,right) + root.val