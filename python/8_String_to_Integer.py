class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        MAX_INT = 2**31-1
        MIN_INT = -2**31
        
        i = 0
        l = len(str)
        while i < l and str[i] == ' ' :
            i += 1
        
   
        res = 0    
        isNeg = False
        
        if i < l and str[i] in ['-', '+']:
            if str[i] == '-':
                isNeg = True
            i += 1
        
        while i<l:
            if str[i].isdigit():
                if res == MAX_INT/10:
                    if isNeg:
                        if int(str[i]) < 9:
                            res = res*10 + int(str[i])
                        else:
                            return MIN_INT
                    else:
                        if int(str[i]) < 8:
                            res = res*1- + int(str[i])
                        else:
                            return MAX_INT
                elif res > MAX_INT/10:
                    if isNeg:
                        return MIN_INT
                    return MAX_INT
                else:
                    res = res * 10 + int(str[i])
                
                i += 1
            else:
                break
        
        res = -res if isNeg else res
        
        return res

sol = Solution()

s = "   "
print sol.myAtoi(s)