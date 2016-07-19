
"""

    294 Flip Game II

    You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, you and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move and therefore the other person will be the winner.

    Write a function to determine if the starting player can guarantee a win.

    For example, given s = "++++", return true. The starting player can guarantee a win by flipping the middle "++" to become "+--+".
"""


class Solution(object):
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        split = s.split("-")
        print split
        resList = map(self.helper , split)
        return  reduce(lambda x , y : x == y , resList)

    def helper(self,s):
        dp = [False, False, True]

        n = len(s)
        if n <= 2:
            return dp[n]
        for l in xrange(3,n+1):
            res = False
            for i in xrange(l/2):
                res |= (dp[i] == dp[l-i-2])
                if res == True:
                    break
            dp.append(res)
        return dp[n]

sol = Solution()
test = "--"
print sol.canWin(test)
