"""
	108. Convert Sorted Array to Binary Search Tree
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
	# recursive
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        def build(i,j):
        	if i < j:
        		m = (i+j)/2

        		root = TreeNode(self.nums[m])
        		root.left = build(i,m)
        		root.right = build(m+1,j)
        		return root
        	return 
        self.nums = nums
        root = build(0,len(self.nums))
        return root

    # iterative
    def sortedArrayToBSTII(self, nums):
    	pass

nums = [1,2,3,4,5,6,7,8]
sol = Solution()
root = sol.sortedArrayToBST(nums)

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