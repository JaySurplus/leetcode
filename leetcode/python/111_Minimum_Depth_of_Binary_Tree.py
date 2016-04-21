"""
	111. Minimum Depth of Binary Tree

	Given a binary tree, find its minimum depth.

	The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

	https://leetcode.com/problems/minimum-depth-of-binary-tree/
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def minDepthII(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
        	return 0

        res = 1
        stack = [root]
        while stack:
        	stack2 = []
        	for temp in stack:
        		if not (temp.left or temp.right):
        			return res
        		if temp.left :
        			stack2.append(temp.left)
        		if temp.right:
        			stack2.append(temp.right)
        	res +=1
        	stack = stack2
        return res

        
    def minDepth(self, root):
    	if not root:
    		return 0
    	if root.left and root.right:
    		return 1+min(self.minDepth(root.left) , self.minDepth(root.right))
    	return 1+ max(self.minDepth(root.left), self.minDepth(root.right))

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)

n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n6
n4.right = n5

sol = Solution()
print sol.minDepth(n1)