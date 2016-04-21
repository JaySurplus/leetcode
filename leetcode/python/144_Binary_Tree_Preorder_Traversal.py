"""
	144. Binary Tree Preorder Traversal

	Given a binary tree, return the preorder traversal of its nodes' values.

	For example:
	Given binary tree {1,#,2,3},

	return [1,2,3].

	https://leetcode.com/problems/binary-tree-preorder-traversal/
"""
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None



class Solution(object):
	def preorderTraversal(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""

		if not root:
			return res
		
		stack = [] 
		res = []
		stack.append(root)

		while stack:
			curr = stack.pop()
			res.append(curr.val)
			if curr.right:
				stack.append(curr.right)
			if curr.left:
				stack.append(curr.left)
		return res

	def preorderTraversalII(self,root):
		if not root:
			return []
		res = []
		stack = []

		dummy = TreeNode('dummy')
		dummy.right = root
		stack.append(dummy)
		while stack:
			temp = stack.pop()
			if temp.right:
				temp = temp.right
				while temp:
					stack.append(temp)
					res.append(temp.val)
					temp = temp.left

		return res



	def preorderTraversalIII(self, root):
		if not root:
			return []
		res = []
		

		def helper(root,res):
			if not root :
				return res
			res.append(root.val)
			helper(root.left, res)
			helper(root.right, res)
			return res
		return helper(root , res)

	def preorderTraversalVI(self, root):
		if not root:
			return []
		res = []
		res += [root.val]
		res += self.preorderTraversalVI(root.left)
		res += self.preorderTraversalVI(root.right)
		return res


def nodeList(n):
	return [TreeNode(i) for i in range(n)]

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)
n7 = TreeNode(7)
n8 = TreeNode(8)
n9 = TreeNode(9)

nL = nodeList(8)


n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.right = n8
n4.right = n6
n5.right = n7


sol = Solution()

import time , copy
s1=time.time()

print sol.preorderTraversalVI(copy.deepcopy(n1))
