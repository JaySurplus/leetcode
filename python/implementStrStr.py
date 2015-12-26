"""
	 
	Implement strStr().

	Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

	https://leetcode.com/problems/implement-strstr/

	Working , but have performance issues.
	Need to be implemented with KMP algorithms.
"""

class Solution(object):
	
    def strStr(self, haystack, needle):
    
        lenH = len(haystack)
        lenN = len(needle)


       	if len(haystack) < len(needle):
       		return -1


        if lenN == 0:
            return 0


       
       	i = 0
        ind = []
       	while i <= lenH - lenN:
            if haystack[i] == needle[0]:
            	pos_match = 1
            	ind = []
            	for j in range(1,lenN):
    				if haystack[i+j] == needle[0]:
    					ind.append(i + j)
    				if haystack[i+j] != needle[j]:
    					break
    				else:
    					pos_match += 1

                if pos_match == lenN:
                    return i
                else:
                    if ind:
                        i = ind.pop(0)
                    else:
                        i += j + 1 
            else:
                if ind:
                    i += ind.pop(0)
                else:
                    i += 1

        return -1

    
    """


	def strStr(self, haystack, needle):
		lenH = len(haystack)
		lenN = len(needle)
		for i in range(lenH -lenN+1):
			if haystack[i:i+lenN] == needle:
				return i
		return -1
	"""

sol = Solution()
haystack = "mississippi"

needle= "issip"
print sol.strStr(haystack, needle)
