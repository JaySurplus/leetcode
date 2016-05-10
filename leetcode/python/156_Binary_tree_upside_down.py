"""
    # Time:  O(n)
# Space: O(1)
#
# Given a binary tree where all the right nodes are either leaf nodes with a sibling
# (a left node that shares the same parent node) or empty, flip it upside down and
# turn it into a tree where the original right nodes turned into left leaf nodes.
# Return the new root.
#
# For example:
# Given a binary tree {1,2,3,4,5},
#
#     1
#    / \
#   2   3
#  / \
# 4   5
#
# return the root of the binary tree [4,5,2,#,#,3,1].
#
#    4
#   / \
#  5   2
#     / \
#    3   1
#
"""
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def upsideDownBinaryTree(self, root):
        p = root
        par = None
        par_right = None

        while p:

            left = p.left
            p.left = par_right
            par_right = p.right
            p.right = par
            par = p
            p = left

        return par

def printTree(root):
    stack = [root]
    while stack:
        curr = stack.pop(0)
        print curr.val
        if curr.left:
            stack.append(curr.left)
        if curr.right:
            stack.append(curr.right)


n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)

n1.right = n3
n1.left = n2
n2.left = n4
n2.right = n5

printTree(n1)

print
sol = Solution()
root = sol.upsideDownBinaryTree(n1)
printTree(root)

