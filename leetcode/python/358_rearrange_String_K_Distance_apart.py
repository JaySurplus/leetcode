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



        ls = [[ks , v] for ks ,  v in dic.iteritems()]
        ls.sort(key = lambda x: x[1],reverse = True)



        i = 0
        maxCount = ls[0][1]

        while i < len(ls):
            if ls[i][1] != maxCount:
                break
            i += 1

        # for s = "aaabbbcc" , k = 3,  the minimal length requires len(abXabXab) == 8 , which is greater then len(s) , 8 .  Thus it is an possible k for s.
        # the minimal required length can be given by:   k * (max_character_count - 1) + number_of_char_with_the_max_count,   in above example, max_character_count = 3, for {a:3,b:3,c:2}
        # and number_of_char_with_the_max_count = 2, for both a , b with count 3. result = 3 * (3-1) + 2 = 8

        if  k * (maxCount-1) + i > len(s):
            return ""

        # create max_character_count sections
        temp = [ls[0][0]] * ls[0][1]



        i = 0

        for l in ls[1:]:
            ks,v = l
            if v == len(temp):
                # For character with count equal to max_character_count, we add the character into every section.
                temp = map(lambda x: x+ks, temp)
            else:
                # For any character count less than the max_character_count, we ignore the last section in temp, beacuse there isn't any section after it.
                while v > 0:
                    temp[i] += ks
                    v -= 1
                    #ignore the last section
                    i = (i+1)%(len(temp)-1)
        return "".join(temp)


sol = Solution()

s = "abeabacdd"
s = "abeabac"
k = 3
k = 2
res = sol.rearrangeString(s,k)

print res



