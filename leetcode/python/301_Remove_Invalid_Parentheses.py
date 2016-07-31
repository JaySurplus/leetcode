"""
    301. Remove Invalid Parentheses
    Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

    Note: The input string may contain letters other than the parentheses ( and ).

    Examples:
        "()())()" -> ["()()()", "(())()"]
        "(a)())()" -> ["(a)()()", "(a())()"]
        ")(" -> [""]
"""

class Solution():
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def isValid(s):
            count = 0
            for c in s:
                if c == '(':
                    count += 1
                elif c == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        level = {s}
        while True:
            valid = filter(isValid,level)
            if valid:
                return valid
            level = {s[:i]+s[i+1:] for s in level for i in xrange(len(s))}
s = "()())()"
sol = Solution()
print sol.removeInvalidParentheses(s)
