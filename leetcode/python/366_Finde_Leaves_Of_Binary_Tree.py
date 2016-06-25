"""
    366 Finde leaves of Binary Tree
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution(object):
    def findLeaves(self, root):
        if not root:
            return []

        self.res = []
        self.helper(root)
        return self.res


    def helper(self, node):
        if not node:
            return -1
        else:
            leftLevel = self.helper(node.left)
            rightLevel = self.helper(node.right)
            level = max(leftLevel, rightLevel) + 1

            if len(self.res) == level:
                self.res.append([])
            self.res[level].append(node.val)
            return level






n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)

n1.right = n3
n1.left = n2
n2.left = n4
n2.right = n5


sol = Solution()
res = sol.findLeaves(n1)
print res
