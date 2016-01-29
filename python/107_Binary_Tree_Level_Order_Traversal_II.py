"""
	107. Binary Tree Level Order Traversal II

	Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).
"""



class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
    	def helper(res,root,height):
    		if not root:
    			return
    		if len(res)==height:
    			res.append([])

    		res[height].append(root.val)
    		helper(res,root.left,height+1)
    		helper(res,root.right,height+1)

    	res = []
    	helper(res, root, 0)
    	return res[::-1]
    def levelOrderBottomII(self, root):
    	res = []
    	temp = [root]

    	while temp :
    		res.append([r.val for r in temp])
    		temp = [ r for node in temp for r in (node.left ,node.right) if r ]
    	return res[::-1]