"""
    364 Nested List Weight Sum II
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
    def depthSumInverseV(self, nestedList):
        if not nestedList:
            return 0

        self.res = 0
        self.temp = 0
        self.helperII(nestedList)

        return self.res

    def helperII(self,nestedList):
        if not nestedList:
            return
        temp = []
        for nI in nestedList:
            if nI.isInteger():
                self.temp+=nI.getInteger()
            else:
                temp += nI.getList()
        self.res += self.temp
        self.helperII(temp)
        return





    def depthSumInverse(self, nestedList):
        if not nestedList:
            return 0

        res = 0
        temp = 0

        while nestedList:
            tempList = []
            for nI in nestedList:

                if nI.isInteger():
                    temp += nI.getInteger()
                else:
                    tempList+=nI.getList()
            res += temp
            nestedList = tempList

        return res




    def depthSumInverseII(self, nestedList):
        if not nestedList:
            return 0

        self.level = 1
        self.l = []
        stack = [nestedList,"#"]
        while stack:
            curr = stack.pop(0)
            if curr == "#":
                if stack:
                    stack.append("#")
                    self.level += 1
            else:
                for nI in curr:
                    if nI.isInteger():
                        self.l.append([nI.getInteger(),self.level])
                    else:
                        stack.append(nI.getList())

        res = reduce(lambda x, y : x +y , [ x[0]*(self.level - x[1] + 1) for x in self.l] , 0)
        return res



    def depthSumInverseIII(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        if not nestedList:
            return 0

        self.maxLevel = 1
        self.l = []
        self.helper(nestedList,1)
        #print self.l , self.maxLevel
        res = 0

        #for n in self.l:
        #    res += n[0] * (self.maxLevel - n[1] + 1)
        res = reduce(lambda x, y : x +y , [ x[0]*(self.maxLevel - x[1] + 1) for x in self.l] , 0)
        return res


    def helper(self, nestedList, level):
        if level > self.maxLevel:
            self.maxLevel = level
        for nI in nestedList:
            if nI.isInteger():
                self.l.append([nI.getInteger(),level])
            else:
                self.helper(nI.getList(),level+1)
        return
