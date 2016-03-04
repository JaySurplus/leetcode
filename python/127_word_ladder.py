"""
    Given two words , find the length of shortest transformation sequence from beginword to endword
    https://leetcode.com/problems/word-ladder/
"""
import string
class Solution(object):
    def ladderLengthII(self, beginWord, endWord,wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        self.res = len(wordList) + 3

        self.dfs([beginWord] , endWord , list(wordList))

        if self.res > len(wordList) + 2:
            return 0
        return self.res

    def dfs(self, currList , endWord, remainList ):
        if len(currList) + 1 >= self.res:
            return
        if self.dist(currList[-1] , endWord):
            self.res = len(currList) + 1
            return
        if len(currList) + 2 >= self.res:
            return
        for i in xrange(len(remainList)):
            if self.dist(currList[-1] , remainList[i]):
                self.dfs(currList+[remainList[i]], endWord, remainList[:i]+remainList[i+1:])
            if len(currList) + 2 > self.res:
                return
        return

    def dist(self,a,b):
        d = 0
        for i in xrange(len(a)):
            if a[i] != b[i]:
                d += 1
                if d > 1:
                    return False
        return d == 1

    def ladderLengthI(self, beginWord, endWord, wordList):

        wordList.add(endWord)
        q = []
        q.append((beginWord, 1))

        while q:
            curr=q.pop(0)
            currword = curr[0]
            currlen = curr[1]
            if currword == endWord:
                return currlen
            for i in range(len(currword)):
                front = currword[:i]
                end = currword[i+1:]

                j = 97
                while j <= ord('z'):
                    if currword[i] != chr(j):
                        nextword = front + chr(j) + end
                        if nextword in wordList:
                            q.append((nextword, currlen+1))
                            wordList.remove(nextword)
                    j += 1
        return 0

    def ladderLength(self, beginWord, endWord, wordList):
        fronts = [{beginWord}, {endWord}]
        levels = [1, 1]
        while fronts[0] and fronts[1]:
            if len(fronts[0]) > len(fronts[1]):
                fronts.reverse()
                levels.reverse()
            newLevel = set()
            for word in fronts[0]:
                for i in xrange(len(beginWord)):
                    for char in string.lowercase:
                        newWord = word[:i] + char  + word[i + 1:]
                        if newWord in fronts[1]:
                            return levels[0] + levels[1]
                        if newWord in wordList:
                            newLevel.add(newWord)
                            wordList.remove(newWord)
                        j += 1
            fronts[0] = newLevel
            levels[0] += 1
        return 0

sol = Solution()


b="hit"
e="cog"
w=set(["hot","dot","dog","lot","log"])
res = sol.ladderLength(b, e, w)
print res

b = 'a'
e = 'c'
w = set(['a', 'b','c'])
res = sol.ladderLength(b, e, w)

print res

