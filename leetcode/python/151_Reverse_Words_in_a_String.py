"""
	151. Reverse Words in a String

	Given an input string, reverse the string word by word.

	For example,
		Given s = "the sky is blue",
		return "blue is sky the".
"""
import sys


class Solution(object):

    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        slist = s
        l = len(slist)
        i = 0
        temp = []
        while i < l:
        	if slist[i] != ' ':
        		j = i + 1
        		while j < l and slist[j] != ' ' :
        			j += 1
        		temp.append(''.join(slist[i:j]))
        		i = j
        	i += 1
    
        lt = len(temp)
        for i in xrange(lt/2):
        	t = temp[i]
        	temp[i] = temp[lt-1-i]
        	temp[lt-1-i] = t
        return ' '.join(temp)


def main(argv=None):
    sol = Solution()
      
    if argv is None:
        if len(sys.argv) == 2:
        	test = sys.argv[1]
        else:
        	test = "this is a test"
        	test = "the sky is blue"
        	
        	
    else:
        test = argv

    
    print "test case : %s" % test
    res = sol.reverseWords(test)
    return res , len(res)
if __name__ == '__main__':
    sys.exit(main())
