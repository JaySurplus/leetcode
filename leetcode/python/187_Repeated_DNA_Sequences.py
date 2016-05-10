"""
    187. Repeated DNA Sequences

    All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

    Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

    For example,

    Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",

    Return:
    ["AAAAACCCCC", "CCCCCAAAAA"].
"""


class Solution(object):

    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        dic = {}
        for i in range(0,len(s)-9):
            if s[i:i+10] in dic:
                dic[s[i:i+10]] += 1
            else:
                dic[s[i:i+10]] = 1

        return [ k for k , v in dic.iteritems() if v > 1 ]

sol = Solution()
s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
print sol.findRepeatedDnaSequences(s)

