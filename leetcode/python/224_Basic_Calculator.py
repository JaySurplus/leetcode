class Solution(object):

    def calculate(self, s):
        res = 0
        num = 0
        sign = 1
        stack = []
        for ss in s:
            if ss.isdigit():
                num = num*10 + int(ss)
            elif ss in ["-" , "+"]:
                res += sign * num
                num = 0
                sign = -1 if ss == "-" else 1
            elif ss == "(":
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif ss == ")":
                res += sign * num
                res *= stack.pop()
                res += stack.pop()

                num = 0
        return res + sign*num


sol = Solution()

test = "11 + 1"
#test = "2-1 + 2 "
#test = "(1+(4+5+2)-3)+((6+8)+(3+3))"
test = "(7)-(0)+(4)"
test = "(7)-(0)+(4)"
print sol.calculate(test)
