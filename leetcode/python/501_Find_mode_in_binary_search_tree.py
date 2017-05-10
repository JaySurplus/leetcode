"""
    501. Find Mode in Binary Search Tree
    https://leetcode.com/problems/find-mode-in-binary-search-tree/?tab=Description
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        self.dic = {}
        self.helper(root)
        z = [(k,self.dic[k]) for k in self.dic.keys()]
        z.sort(key=lambda x:x[1],reverse=True)
        return [k[0] for k in z if k[1] == z[0][1]]

    def helper(self, node):
        if not node:
            return
        if node.val in self.dic:
            self.dic[node.val] += 1
        else:
            self.dic[node.val] = 1
        self.helper(node.left)
        self.helper(node.right)
        return

N1 = TreeNode(1)
N2 = TreeNode(2)
N3 = TreeNode(2)

N1.right = N2
N2.left = N3

sol = Solution()
print sol.findMode(N1)
