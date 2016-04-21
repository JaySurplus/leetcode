"""
	109. Convert Sorted List to Binary Search Tree

	Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.


"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
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
        self.nums = []
        while head:
        	self.nums.append(head.val)
        	head = head.next

    
        root = build(0,len(self.nums))
        return root

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n6 = ListNode(6)
n7 = ListNode(7)
n8 = ListNode(8)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
n7.next = n8




sol = Solution()
root = sol.sortedListToBST(n1)

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