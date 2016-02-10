"""
	113. Path Sum II

	Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

	For example:
	Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
	return
	[
   		[5,4,11,2],
   		[5,8,4,5]
	]
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        def dfs(root,s,temp):
        	if not root:
        		return
        
        	if not root.left and not root.right and s == root.val :
        		
        		self.res.append(temp+[root.val])
        		return
        	
        	dfs(root.left, s - root.val , temp +[root.val])
        	dfs(root.right, s - root.val , temp +[root.val])

        self.res = []
        dfs(root, sum , [])
        return self.res
    def pathSumI(self, root , sum):
    	if not root:
    		return []
    	stack = [root]


n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n44 = TreeNode(4)
n5 = TreeNode(5)
n55 = TreeNode(5)
n6 = TreeNode(6)
n7 = TreeNode(7)
n8 = TreeNode(8)
n9 = TreeNode(9)
n10 = TreeNode(10) 
n11 = TreeNode(11)
n13 = TreeNode(13)

n5.left = n4
n5.right = n8
n4.left = n11
n11.left = n7
n11.right = n2
n8.left = n13
n8.right = n44
n44.left = n55
n44.right = n1

sol =  Solution()
print sol.pathSum(n5,22)
