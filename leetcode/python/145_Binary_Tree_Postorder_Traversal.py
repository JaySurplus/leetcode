"""
	145. Binary Tree Postorder Traversal 


	Given a binary tree, return the postorder traversal of its nodes' values.

	For example:
	Given binary tree {1,#,2,3},
   	1
     \
      2
     /
   	3
	return [3,2,1].

	Note: Recursive solution is trivial, could you do it iteratively?

	https://leetcode.com/problems/binary-tree-postorder-traversal/

"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        if not root:
        	return []

        res = []
        stack = []
        
        stack.append(root)
        while stack:
        	curr = stack.pop()
        	if curr == '#':
        		res.append(stack.pop().val)
        	else:
        		
        		if  curr.right or curr.left:
        			stack.append(curr)
        			stack.append('#')
        			if curr.right:
        				stack.append(curr.right)
        			if curr.left:
        				stack.append(curr.left)
        		else:
        			res.append(curr.val)
        return res


    def postorderTraversalII(self, root):
    	"""
    	reverse
    	"""
    	if not root:
    		return []
    	res = []
    	stack = []
    	stack.append(root)

    	while stack:
    		curr = stack.pop()
    		res.append(curr.val)

    		if curr.left:
    			stack.append(curr.left)
    		if curr.right:
    			stack.append(curr.right)
    	res.reverse()
    	return res


    def postorderTraversalIII(self, root):
    	"""
    	recursive
    	"""
    	if not root:
    		return []
    	res = []
    	res += self.postorderTraversalIII(root.left)
    	res += self.postorderTraversalIII(root.right)
    	res += [root.val]
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
n3.left = n6
n4.right = n7
n5.left = n8
n5.right = n9

sol = Solution()
print sol.postorderTraversal(n1)