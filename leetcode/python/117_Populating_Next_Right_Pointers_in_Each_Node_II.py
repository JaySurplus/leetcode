"""
	117. Populating Next Right Pointers in Each Node II

	Follow up for problem "Populating Next Right Pointers in Each Node".

	What if the given tree could be any binary tree? Would your previous solution still work?

	Note:

	You may only use constant extra space.
	For example,
	Given the following binary tree,
         1
        / \
       2   3
      / \   \
     4   5   7
	After calling your function, the tree should look like:
         1 -> NULL
        / \
       2 ->3 -> NULL
      / \   \
     4-> 5 ->7 -> NULL
"""

# Definition for binary tree with next pointer.
class TreeLinkNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if not root:
            return
        curr = root
        while curr:
            f_next = None
            pre = None
            while curr:
                if not f_next:
                    f_next = curr.left if curr.left else curr.right
                if curr.left:
                    if pre:
                        pre.next = curr.left
                    pre = curr.left
                if curr.right:
                    if pre:
                        pre.next = curr.right
                    pre = curr.right
                curr = curr.next
            curr = f_next



