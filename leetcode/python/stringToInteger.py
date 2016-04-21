#!/usr/bin/python
'''
https://leetcode.com/submissions/detail/38595104/
'''

class Solution(object):
    def myAtoi(self, str):
        result = 0
        if len(str)==0:
            return 0
        neg = False
        i = 0
        while (str[i] == ' '):
            i+=1
        if str[i] in ['+','-']:
            neg = (str[i] == '-')
            i+=1
        for j in range(i , len(str)):
            if str[j].isdigit():
                if result == 214748364:
                    if neg:
                        if int(str[j]) < 9:
                            result = result * 10 + int(str[j])
                        else:
                            return -2147483648
                    else:
                        if int(str[j]) < 8:
                            result = result * 10 + int(str[j])
                        else:
                            return 2147483647

                elif result > 214748364:
                    if neg:
                        return -2147483648
                    return 2147483647
                    
                else:
                    result = result * 10 + int(str[j])
            else:
                break

        if neg:
            result = -result
        return result       


test = Solution()


print test.myAtoi('123456')       
print test.myAtoi('-1234')
print test.myAtoi('-1234')
print test.myAtoi('   010')
print test.myAtoi('2147483648')
print test.myAtoi('-2147483648')





