"""
	112. Path Sum

	Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

	For example:
	Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
	return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """

        if not root:
        	return False
        if not root.left and not root.right:
        	return root.val == sum
        return self.hasPathSum(root.left , sum - root.val) or self.hasPathSum(root.right , sum - root.val)
        

sol = Solution()

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)


n1.right = n2
n2.left = n3
n3.right = n5
n3.left = n4

print sol.hasPathSum(n1,11)