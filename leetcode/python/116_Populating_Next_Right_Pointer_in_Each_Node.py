
"""
116. Populating Next Right Pointers in Each Node

Given a binary tree

    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
For example,
Given the following perfect binary tree,
        1
       / \
      2   3
     / \ / \
    4  5 6  7
After calling your function, the tree should look like:
        1 -> NULL
       / \
      2 ->3 -> NULL
     / \  / \
    4->5->6->7 -> NULL
"""

# Definition for binary tree with next pointer.
class TreeLinkNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution(object):
    def connectII(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if root == None:
            return
        que = []
        que.append(root)
        count = 0
        while que:
            node = que.pop(0)
            if node.left:
                que.append(node.left)
                que.append(node.right)
            count += 1
            node.next = None if count & (count+1) == 0 else que[0]

    def connect(self, root):
        """
    	if not root:
    		return
    	pre = root
    	curr = None
    	while pre.left:
    		curr = pre
    		while curr:
    			curr.left.next = curr.right
    			if curr.next:
    				curr.right.next = curr.next.left
    			curr = curr.next
    		pre = pre.left
        """
        if not root:
            return
        pre = root
        curr = None
        while pre.left:
            curr = pre
            while curr:
                curr.left.next = curr.right
                if curr.next:
                    curr.right.next = curr.next.left
                curr = curr.next
            pre = pre.left





