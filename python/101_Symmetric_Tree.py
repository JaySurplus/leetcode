"""
	101. Symmetric Tree

	Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

	For example, this binary tree is symmetric:

    	1
       / \
  	  2   2
 	 / \ / \
	3  4 4  3
	But the following is not:
    	1
       / \
  	  2   2
   	   \   \
   	    3   3


"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
   
        def isSameTree(p, q):
        	if p and q:
        		if p.val == q.val:
        			return isSameTree(p.right , q.left) and isSameTree(p.left, q.right)
        	if not (p or q):
        		return True
        	return False

        if not root:
        	return True

        return isSameTree(root.left, root.right)

    def isSymmetricII(self, root):
    	if not root:
    		return True
    	stack = []
    	stack.append((root.left, root.right))
    	while stack:
    		l , r = stack.pop()

    		if l and r:
    			if l.val == r.val:
    				stack.append((l.left , r.right))
    				stack.append((l.right , r.left))
    			else:
    				return False
    		elif l or r:
    			return False
    	return True



n1 = TreeNode(1)
n2 = TreeNode(2)
n22 = TreeNode(2)
n3 = TreeNode(3)
n33 = TreeNode(3)
n4 = TreeNode(4)
n44 = TreeNode(4)

n1.left = n2
n1.right = n22
n2.left = n3
#n22.left = n44
#n2.right = n4
n22.left = n33
#n22.left = n33

sol = Solution()
print sol.isSymmetricII(n1)

