"""
	94. Binary Tree Inorder Traversal

	Given a binary tree, return the inorder traversal of its nodes' values.

	For example:
	Given binary tree {1,#,2,3},
   	1
     \
     2
     /
    3
	return [1,3,2].

	https://leetcode.com/problems/binary-tree-inorder-traversal/

"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
	def inorderTraversal(self, root):
		stack = []
		curr = root
		res = []
		while True:
			while curr :
				stack.append(curr)
				curr = curr.left
			
			if len(stack) > 0:
				curr = stack.pop()
				res.append(curr.val)
				curr = curr.right
			else:
				break
		return res
	def inorderTraversalII(self,root):
		def rec(node):
			if not node:
				return
			rec(node.left)
			self.res.append(node.val)
			rec(node.right)
			return
		self.res = []
		rec(root)
		return self.res

    	

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)

n1.left =n2
n1.right = n3
n2.left = n4
n2.right = n5

sol = Solution()
print sol.inorderTraversalII(n1)


