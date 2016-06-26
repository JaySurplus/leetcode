"""
    358. Rearrange String k Distance Apart



"""



class Solution(object):
    def rearrangeString(self, s, k):
        """
        :type str: str
        :type k: int
        :rtype: str
        """
        dic = {}

        for c in s:
            dic[c] = dic.get(c,0) + 1



        l = [[ks , v] for ks ,  v in dic.iteritems()]
        l.sort(key = lambda x: x[1],reverse = True)


        temp = [l[0][0]] * l[0][1]
        i = 0
        tl = l[0][1]

        while i < len(l):
            if l[i][1] != tl:
                break
            i += 1

        if  k * (tl-1) + i > len(s):
            return ""

        l.pop(0)

        i = 0
        while l:
            ks,v = l.pop(0)
            if v == len(temp):
                temp = map(lambda x: x+ks, temp)
            else:
                while v > 0:
                    temp[i] += ks
                    v -= 1
                    #ignore the last section
                    i = (i+1)%(len(temp)-1)
        return "".join(temp)


sol = Solution()

s = "abeabacdd"
#s = "abeabac"
k = 3
k = 5
res = sol.rearrangeString(s,k)

print res



