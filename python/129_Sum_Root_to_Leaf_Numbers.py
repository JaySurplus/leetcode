"""
	129. Sum Root to Leaf Numbers

	Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

	An example is the root-to-leaf path 1->2->3 which represents the number 123.

	Find the total sum of all root-to-leaf numbers.

	For example,

    	1
   	   / \
      2   3
	The root-to-leaf path 1->2 represents the number 12.
	The root-to-leaf path 1->3 represents the number 13.

	Return the sum = 12 + 13 = 25.
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumNumbers_rec(self,root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # It is possible overflow
        if not root:
            return 0
        self.res = 0
        self.dfs(root,0)

        return self.res

    def dfs(self, root , val):
    	if root and val < 2**31-1 and self.res < 2**31-1:
    		if val*10 + root.val < 2**31-1:
    			self.dfs(root.left, val*10 + root.val)
    			self.dfs(root.right, val*10 +root.val)
    			if not root.left and not root.right:
    				self.res += val*10 + root.val
    		else:
    			self.res = 2**31-1
    		return
        
    # Non-recursive
    def sumNumbers(self, root):
    	if not root:
    		return 0


sol = Solution()

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)

n1.left = n2

n2.right = n3
n3.right = TreeNode(5)
n3.left = TreeNode(5)
print sol.sumNumbers_rec(n1)

        
