class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
        	return s
        result=['']*numRows
        rang = (numRows-1)<<1
        for i in range(len(s)):
        	pos = i%rang
        	if pos<= numRows-1:
        		#print s[i] , i
        		result[pos]+=s[i]
        	else:
        		result[-1 * (pos) + rang]+=s[i]
        result = ''.join(result)
        #Test


        return result



test = Solution()
result = test.convert("ABCDE", 4)

print result
print test.convert('PAYPALISHIRING',3)
print 'PAHNAPLSIIGYIR'


