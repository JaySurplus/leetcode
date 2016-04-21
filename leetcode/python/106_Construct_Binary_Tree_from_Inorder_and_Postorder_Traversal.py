"""
	106. Construct Binary Tree from Inorder and Postorder Traversal

	Given inorder and postorder traversal of a tree, construct the binary tree.

	https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        def rebuild(i , j ):
        	if i < j:
        		root = TreeNode(postorder.pop())
        		ind = self.dic[root.val]

        		root.right = rebuild(ind+1,j)
        		root.left = rebuild(i,ind)
        		return root
        	return
        
        self.dic = {}

        for k in range(len(inorder)):
        	self.dic[inorder[k]] = k
        root = rebuild(0,len(inorder))
        return root

sol = Solution()


inorder =  [1,2,5,6,7,8,9,12,15,20]
postorder=  [1,2,6,8,7,5,12,20,15,9]


root = sol.buildTree(inorder , postorder)

def pre(root ):
	def p(root):
		if not root:
			return
		res.append(root.val)
		p(root.left)
		p(root.right)
		return
	res = []
	p(root)
	return res

def ino(root):
	def i(root):
		if not root:
			return
		i(root.left)
		res.append(root.val)
		i(root.right)
		return
	res = []
	i(root)
	return res

def pos(root):
	def q(root):
		if root:
			
			q(root.left)
			q(root.right)
			res.append(root.val)
			#print root.val
		return 
	res = []
	q(root)
	return res
print 
print pre(root)
print ino(root)
print pos(root)

