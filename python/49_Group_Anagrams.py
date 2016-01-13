"""
	49. Group Anagrams


	Given an array of strings, group anagrams together.

	Note:
		For the return value, each inner list's elements must follow the lexicographic order.
		All inputs will be in lower-case.
"""

chr_primes= [5, 71, 37, 29, 2, 53, 59, 19, 11, 83, 79, 31, 43, 13, 7, 67, 97, 23, 17, 3, 41, 73, 47, 89, 61, 101]



def getStrSig(s):
      ord_a = ord('a')
      hash = 1
      for c in s:
          hash *= chr_primes[ ord(c) - ord_a ]
      return hash


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        

        dic = {}

        for s in strs:
        	sort = getStrSig(s)
        	dic[sort] = [s] if sort not in dic else dic[sort] + [s]

        res = []
        for key , val in dic.iteritems():
        	res.append(sorted(val))
        return res

sol =Solution()

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

print sol.groupAnagrams(strs)

