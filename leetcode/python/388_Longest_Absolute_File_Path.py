"""
    388 Longest Absolute File Path
    https://leetcode.com/problems/longest-absolute-file-path/
"""

class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        input = input.split("\n")
        res = 0
        tempLen = 0
        stack = []
        while input:
            t = input.pop(0)
            ts = t.split('\t')
            while stack and stack[-1][0] >= len(ts)-1:
                tt = stack.pop()
                tempLen -= tt[1]

            if len(ts[-1].split(".")) > 1:
                res = max(res,tempLen+len(ts[-1]))
            else:
                stack.append((len(ts)-1,len(ts[-1])+1))
                tempLen += len(ts[-1])+1
        return res


if __name__ == '__main__':
    sol = Solution()
    input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
    input = "a\n\tb.txt\na2\n\tb2.txt"
    res = sol.lengthLongestPath(input)
    print res



