"""
	104. Maximum Depth of Binary Tree

	Given a binary tree, find its maximum depth.

	The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None




class Solution(object):
	def maxDepthI(self, root):
		

		def md(node , depth):
			if not node:
				return
			if node.left:
				if depth >= self.res :
					self.res += 1
				md(node.left , depth+1)
			if node.right :
				if depth >= self.res:
					self.res += 1
				md(node.right , depth+1)
			return

		if not root:
			return 0

		self.res = 0
		md(root , 0)
		return self.res

	def maxDepthII(self, root):
		if not root:
			return 0
	
		stack = [root]
		stack2 = []
		res = 1
		while stack:
			if stack[-1].left or stack[-1].right:
				res += 1
				while stack:
					t = stack.pop()
					if t.left:
						stack2.append(t.left)
					if t.right:
						stack2.append(t.right)
				stack = stack2
				stack2 = []
			else:
				stack.pop()		
		return res

	def maxDepth(self,root):
		if not root :
			return 0
		return max(self.maxDepth(root.left) , self.maxDepth(root.right)) + 1

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
n9.left = n4
n9.right = n2

n1


sol = Solution()
print sol.maxDepth(n1)