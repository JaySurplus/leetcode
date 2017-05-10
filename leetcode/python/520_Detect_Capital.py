"""
    520. Detect Capital
    https://leetcode.com/problems/detect-capital/?tab=Description
"""
class Solution(object):
    def detectCapitalUseII(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if not word:
            return True
        def tester(i,w,lower=True):
            if i == len(w):
                return True
            if w[i].islower():
                if lower:
                    return tester(i+1,w,lower)
                return False
            if w[i].isupper():
                if not lower:
                    return tester(i+1,w,lower)
                return False
            return False

        if word[0].islower():
            lower = True
        else:
            lower = False

        if tester(1,word,lower):
            return True

        if word[0].isupper():
            return tester(1,word,lower=True)

        return False

    def detectCapitalUse(self, word):
        total = sum(map(lambda x: x.isupper(), word))
        return total == 0 or total == len(word) or (total == 1 and word[0].isupper())
sol = Solution()
word = "Leetcodefds"

print sol.detectCapitalUseII(word)




