"""
    Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.


    Example 1
    Input: "2-1-1".

    ((2-1)-1) = 0
    (2-(1-1)) = 2
    Output: [0, 2]


    Example 2
    Input: "2*3-4*5"

    (2*(3-(4*5))) = -34
    ((2*3)-(4*5)) = -14
    ((2*(3-4))*5) = -10
    (2*((3-4)*5)) = -10
    (((2*3)-4)*5) = 10
    Output: [-34, -14, -10, -10, 10]

"""
import operator, re
ops = {'+': operator.add, '-': operator.sub, '*': operator.mul}

class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        nums = [int(x) for x in re.findall(r'[0-9]+',s)]
        opers = re.findall(r'\+|\-|\*',s)

        n, DP = len(nums), {}
        for i in range(n):
            DP[i,i] = [nums[i]]

        for i in range(n-1):
            DP[i,i+1] = [ops[opers[i]](nums[i],nums[i+1])]

        for k in range(3,n+1):
            for i in range(n-k+1):
                j = i + k -1
                DP[i,j] = []
                for v in range(i,j):
                    left = DP[i,v]
                    right = DP[v+1,j]
                    for e1 in left:
                        for e2 in right:
                            DP[i,j].append(ops[opers[v]](e1,e2))
        print DP
        return DP[0,n-1]



sol = Solution()

s = "2*3-4*5"
res = sol.diffWaysToCompute(s)




