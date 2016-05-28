"""
    199. Binary Tree Right Side View
    Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

    For example:
    Given the following binary tree,
        1            <---
      /   \
     2     3         <---
      \     \
       5     4       <---
    You should return [1, 3, 4].
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        res = []
        stack = []
        dic = {}
        stack.append(root )

        while stack:

            node= stack[0]
            res.append(node.val)

            temp = list(stack)
            stack = []

            for node in temp:
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
        return res



    def rightSideViewII(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        prevLvl = [root]
        ret = []

        while prevLvl:
            ret.append(prevLvl[0].val)
            T = list(prevLvl)
            prevLvl[:] = []
            for node in T:
                if node.right:
                    prevLvl.append(node.right)
                if node.left:
                    prevLvl.append(node.left)
        return ret


n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)

n1.left = n2
n1.right = n3

n2.right = n4
n3.right = n4

sol = Solution()
res = sol.rightSideViewII(n1)
print res
