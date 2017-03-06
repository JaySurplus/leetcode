"""
    508. Most Frequent Subtree Sum
    https://leetcode.com/problems/most-frequent-subtree-sum/?tab=Description
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        self.dic = {}
        def helper(node):
            if not node:
                return 0
            v = node.val + helper(node.left) + helper(node.right)
            if v not in self.dic:
                self.dic[v] = 0
            self.dic[v] += 1
            return v

        helper(root)
        li = [[k,self.dic[k]] for k in self.dic.keys()]
        li.sort(key = lambda x: x[1], reverse = True)

        maxV = li[0][1]
        #i = 0
        #res = []
        #while i < len(li) and li[i][1] == maxV:
        #    res.append(li[i][0])
        #    i += 1
        #return res
        l = 0
        r = len(li)
        while l < r:
            m = (l+r)/2
            if li[m][1] == maxV:
                l = m + 1
            else:
                r = m

        return [v[0] for v in li[:l]]




N1 = TreeNode(1)
N2 = TreeNode(2)
N3 = TreeNode(3)
Neg3 = TreeNode(-3)
N4 = TreeNode(4)
N5 = TreeNode(5)
Neg5 = TreeNode(-5)
N6 = TreeNode(6)
N7 = TreeNode(7)



N5.left = N2
N5.right = Neg5

sol = Solution()
print sol.findFrequentTreeSum(N5)
