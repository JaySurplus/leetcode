"""
	102. Binary Tree Level Order Traversal

	Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
"""

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution(object):
	def levelOrder(self,root):
		if not root:
			return []
		stack = [root]
		stack2 = []
		res = []
		temp = []
		while stack:
			node = stack[0]
			stack = stack[1:]
			temp.append(node.val)
			
			if node.left:
				stack2.append(node.left)

			if node.right:
				stack2.append(node.right)
			

			if not stack:
				res.append(temp)
				temp = []
				stack , stack2 = stack2, stack
		return res

	def levelOrderII(self,root):

		def helper(res, root , height):
			if len(res) == height:
				res.append([])
			res[height].append(root.val)
			if root.left:
				helper(res, root.left, height+1)
			if root.right:
				helper(res, root.right, height+1)


		if not root:
			return []
		
		res = []
		helper(res, root, 0)
		return res







n1 = TreeNode(1)
n2 = TreeNode(2)
n22 = TreeNode(2)
n3 = TreeNode(3)
n33 = TreeNode(3)
n4 = TreeNode(4)
n44 = TreeNode(4)
n9 = TreeNode(9)
n20 =TreeNode(20)
n15 = TreeNode(15)
n7 = TreeNode(7)

n3.left = n9
n3.right = n20
n20.left = n15
n20.right = n7

sol = Solution()
print sol.levelOrderII(n3)
 
