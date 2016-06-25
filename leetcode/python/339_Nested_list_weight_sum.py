"""
    339. Nested List Weight Sum
"""

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution(object):
    def depthSum(self, nestedList):
        depth = 1
        nestedList.append("#")
        res = 0
        while nestedList:

            curr = nestedList.pop(0)
            if curr == "#":
                depth += 1
                if nestedList:
                    nestedList.append("#")
            else:
                if curr.isInteger():
                    res += curr.getInteger() * depth
                else:
                    nestedList+=curr.getList()
        return res



    def depthSumRe(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        self.res = 0
        depth = 1

        self.helper(nestedList,1)
        return self.res

    def helper(self, nestedList, depth):

        for nI in nestedList:

            if nI.isInteger():
                self.res += depth * nI.getInteger()
            else:
                self.helper(nI.getList() , depth+1)
        return




