"""
	114. Flatten Binary Tree to Linked List

	Given a binary tree, flatten it to a linked list in-place.

	For example,
	Given

         1
        / \
       2   5
      / \  / \
     3  4  7  6
	The flattened tree should look like:
   	1
     \
      2
       \
        3
         \
          4
           \
            5
             \
              6

"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """

        def dfs(root):
        	if not root:
        		return None

        	lend = dfs(root.left)
        	rend = dfs(root.right)
        	
        	if not lend and not rend:
        		return root
        	if not lend:
        		return rend  
        	if not rend:
        		rend = lend
        	lend.right= root.right
        	root.right = root.left
        	root.left = None

        	return rend
        dfs(root)

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

n1.left = n2
n2.left = n3

n2.right = n4

n1.right = n5
n5.right = n6
#n5.left = n7
#n7.left = n9
#n7.right = n10

sol = Solution()
sol.flatten(n1)



while n1:
	print n1.val
	n1 = n1.right

