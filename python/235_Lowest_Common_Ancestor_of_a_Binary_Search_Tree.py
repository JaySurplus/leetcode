"""
	235. Lowest Common Ancestor of a Binary Search Tree
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestorII(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root :
        	return None

        if (p.val - root.val ) * (q.val - root.val) <= 0:
        	return root
        elif q.val - root.val > 0:
        	return self.lowestCommonAncestorII(root.left , p, q)
        else:
        	return self.lowestCommonAncestorII(root.right , p, q)
    def lowestCommonAncestor(self, root, p, q):
    	if not root:
    		return None
    	while (p.val - root.val ) * (q.val - root.val) > 0:
    		root = root.left if q.val < root.val else root.right
    	return root