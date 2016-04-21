"""
	100. Same Tree

	Given two binary trees, write a function to check if they are equal or not.

	Two binary trees are considered equal if they are structurally identical and the nodes have the same value.

	https://leetcode.com/problems/same-tree/
"""
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p and q:
            if p.val == q.val:
                return self.isSameTree(p.right , q.right) and self.isSameTree(p.left, q.left)
        if not (p or q):
            return True
        return False