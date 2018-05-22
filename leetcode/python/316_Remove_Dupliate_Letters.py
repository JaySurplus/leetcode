#!python
# Given a string which contains only lowercase letters, remove duplicate letters so that every letter appear once and only once. 
# You must make sure your result is the smallest in lexicographical order among all possible results.


class Solution:
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """

        visited = {}
        count = {}
        for c in s:
            count[c] = 1 if c not in count else count[c] + 1
        visited = {c: False for c in count}
        
        stack = []
        for c in s:
            count[c] -= 1
            if not visited[c]:
                while stack and count[stack[-1]] > 0 and stack[-1] > c:
                    visited[stack[-1]] = False
                    stack.pop()
            stack.append(c)
            visited[c] = True
        return "".join(stack)




if __name__ == "__main__":
    ss = ["bcabc", "cbacdcbc"]

    sol = Solution()
    for s in ss:
        print("String is %s, result is %s" % (s, sol.removeDuplicateLetters(s)))
    