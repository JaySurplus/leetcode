#!/usr/local/bin/python3
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
        slist = []

        pre = " "
        for i in range(len(s) - 1, -1, -1):
            if s[i] != " " or s[i] == " " and pre != " ":
                slist.append(s[i])
                pre = s[i]

        l = len(slist)
        j = 0
        for i in range(l + 1):
            if i == l or slist[i] == ' ':
                if i < l - 1 and slist[i + 1] == ' ':
                    continue
                k = j
                while k < (i + j) / 2:
                    temp = slist[k]
                    slist[k] = slist[i - 1 - k + j]
                    slist[i - 1 - k + j] = temp
                    k += 1
                j = i + 1

        return ''.join(slist)

    def reverseWordsII(self, s):
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
                while j < l and slist[j] != ' ':
                    j += 1
                temp.append(''.join(slist[i:j]))
                i = j
            i += 1

        lt = len(temp)
        for i in range(lt / 2):
            t = temp[i]
            temp[i] = temp[lt - 1 - i]
            temp[lt - 1 - i] = t
        return ' '.join(temp)


def main(argv=None):
    sol = Solution()

    if argv is None:
        if len(sys.argv) == 2:
            test = sys.argv[1]
        else:
            test = "this is a test"
            #test = " "

    else:
        test = argv

    print ("test case : %s" % test)
    res = sol.reverseWords(test)
    return res, len(res)
if __name__ == '__main__':
    sys.exit(main())
