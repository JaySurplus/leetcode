"""
    150. Evaluate Reverse Polish Notation

    Evaluate the value of an arithmetic expression in Reverse Polish Notation.

    Valid operators are +, -, *, /. Each operand may be an integer or another expression.

    Some examples:
        ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
        ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
"""
class Solution(object):

    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        def operations(a, b, operator):
            if operator == '+':
                return a + b
            if operator == '-':
                return a - b
            if operator == '*':
                return a * b
            if operator == '/':
                return int(1. * a / b)

        temp = []
        for i in xrange(len(tokens)):
            if tokens[i] not in ['+', '-', '*', '/']:
                temp.append(int(tokens[i]))
            else:
                b = temp.pop()
                a = temp.pop()
                temp.append(operations(a, b, tokens[i]))
            print temp
        return temp.pop()

    def evalRPNII(self, tokens):
        stack = []
        ops = {'+': lambda x, y: x + y,
               '-': lambda x, y: x - y,
               '*': lambda x, y: x * y,
               '/': lambda x, y: x / y}
        for s in tokens:
            try:
                stack.append(float(s))
            except:
                b = stack.pop()
                a = stack.pop()
                stack.append(int(ops[s](a, b)))
        return int(stack[-1])

sol = Solution()
test = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
# test = ["4","-2","/","2","-3","-","-"]
print sol.evalRPNII(test)
