"""
	103. Binary Tree Zigzag Level Order Traversal
"""

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution(object):
	def zigzagLevelOrder(self,root):
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

	def zigzagLevelOrderII(self,root):

		def helper(res, root , height ,b):
			if len(res) == height:
				res.append([])

			if not b:
				res[height].append(root.val)
			else:
				
				res[height] = [root.val] + res[height] 

			
			if root.left:
				helper(res, root.left, height+1, not b)
			if root.right:
				helper(res, root.right, height+1, not b)
	

		if not root:
			return []
		
		b = False
		res = []
		helper(res, root, 0 , b)
		"""
		i = 1
		while i < len(res):
			res[i] = res[i][::-1]
			i += 2
		"""
		return res
	def zigzagLevelOrderIII(self,root):

		def helper(res, root , height):
			if len(res) == height:
				res.append([])

			
			res[height].append(root.val)
			
			
			

			
			if root.left:
				helper(res, root.left, height+1 )
			if root.right:
				helper(res, root.right, height+1)
	

		if not root:
			return []
		
		
		res = []
		helper(res, root, 0 )
		
		i = 1
		while i < len(res):
			res[i] = res[i][::-1]
			i += 2
	
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
n9.left = n4
n9.right = n2




sol = Solution()
print sol.zigzagLevelOrderIII(n3)