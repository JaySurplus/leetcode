class Solution:
 
# @param A, a list of integer
# @return an integer
	def lengthOfLongestSubstring(self, s):
		length = len(s)
		dic = {}
		Max = 0
		start = 0
		for i in range(length):
			if s[i] in dic:
				if dic[s[i]] >= start:
					start = dic[s[i]]+1
			dic[s[i]] = i
			Max = max(Max,i-start+1)
			#print 'Start: %d , current: %d, MAX: %d'%(start,i,Max)
			#for k ,v in dic.iteritems():
			#	print '\t', k , v
		return Max

test = Solution()

print test.lengthOfLongestSubstring('aaaaa')
print test.lengthOfLongestSubstring('ab')
print test.lengthOfLongestSubstring('abc')
print test.lengthOfLongestSubstring('aabcdef')
print test.lengthOfLongestSubstring('abcabc')
print test.lengthOfLongestSubstring('tmmzuxt')
print test.lengthOfLongestSubstring('qwnfenpglqdq')