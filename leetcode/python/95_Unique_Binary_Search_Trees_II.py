"""
	95. Unique Binary Search Trees II 

	Given n, generate all structurally unique BST's (binary search trees) that store values 1...n.

	For example,
	Given n = 3, your program should return all 5 unique BST's shown below.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
   https://leetcode.com/problems/unique-binary-search-trees-ii/
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @return a list of tree node
    def dfs(self, start, end):
        if start > end: return [None]
        res = []
        for rootval in range(start, end+1):
            LeftTree = self.dfs(start, rootval-1)
            RightTree = self.dfs(rootval+1, end)
            for i in LeftTree:
                for j in RightTree:
                    root = TreeNode(rootval)
                    root.left = i
                    root.right = j
                    res.append(root)
        return res
    def generateTrees(self, n):
        return self.dfs(1, n)

sol = Solution()
res = sol.generateTrees(3)
for i in res:
	print i.val
	#print i.left.val
	print i.right.val