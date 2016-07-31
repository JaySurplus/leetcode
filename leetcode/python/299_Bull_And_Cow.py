"""
    299. Bulls and Cows

"""
class Solution(object):
    def getHint(self,secret,guess):
        n_bull = 0
        dic = {}
        for i in xrange(len(secret)):
            if secret[i] == guess[i]:
                n_bull += 1
            else:
                if guess[i] in dic:
                    dic[guess[i]][1] += 1
                else:
                    dic[guess[i]] = [0,1]
                if secret[i] in dic:
                    dic[secret[i]][0] += 1
                else:
                    dic[secret[i]] = [1,0]

        n_cow = 0
        for k in dic:
            n_cow += min(dic[k][0],dic[k][1])

        return "%dA%dB" %(n_bull,n_cow)

sol = Solution()
s = "1123"
f = "2113"
print sol.getHint(s,f)
