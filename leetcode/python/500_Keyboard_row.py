"""
    500. Keyboard Row
    https://leetcode.com/problems/keyboard-row/?tab=Description
"""
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        s1 = set(['q','w','e','r','t','y','u','i','o','p'])
        s2 = set(['a','s','d','f','g','h','j','k','l'])
        s3 = set(['z','x','c','v','b','n','m'])

        res = []
        for word in words:
            t = word[0].lower()
            if t in s1:
                row = s1
            elif t in s2:
                row = s2
            else:
                row = s3
            i = 0
            while i < len(word):
                if word[i].lower() not in row:
                    break
                i += 1
            if i == len(word):
                res.append(word)
        return res


sol = Solution()
words = ["Hello","Alaska","Dad","Peace"]
print sol.findWords(words)
