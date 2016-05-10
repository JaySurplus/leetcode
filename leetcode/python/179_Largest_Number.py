"""
    179. Largest Number

    Given a list of non negative integers, arrange them such that they form the largest number.

    For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

    Note: The result may be very large, so you need to return a string instead of an integer.
"""


class Solution(object):
    # @param {integer[]} nums
    # @return {string}


    def largestNumber(self, nums):
        r = ''.join(sorted(map(str, nums), lambda x, y: [1, -1][x + y > y + x]))
        return r.lstrip('0') or '0'


    def largestNumberII(self, nums):
        res = [""]
        dic = {}
        for num in nums:
            if str(num) not in dic.keys():
                dic[str(num)] = 1
            else:
                dic[str(num)] += 1

        if len(dic.keys()) == 1 and '0' in dic.keys():
            return '0'

        root = self.make_trie(nums)
        self.iterateTrie(res, "",  root , dic)
        print root

        return res[0]

    def iterateTrie(self, res , temp ,  root , dic ):
        flag = True

        for i in range(9,-1,-1):
            if str(i) in root:
                if temp and (str(i) > temp[-1] or  str(i) < temp[-1]):
                    self.iterateTrie(res, temp+str(i), root[str(i)] , dic )
                else:
                    print temp
                    if temp in dic:
                        res[0] += temp*dic[temp]
                    self.iterateTrie(res, temp+str(i), root[str(i)] , dic )

        if temp in dic.keys():
            if temp[-1] > temp[0] :
                res[0] += temp*dic[temp]
            else:
                i = len(temp)-1
                while i > 0:
                    if temp[:i] in dic.keys():
                        res[0] += temp[:i]*dic[temp[:i]]
                        del dic[temp[:i]]
                        i -= 1
                    else:
                        break
                res[0] += temp*dic[temp]
        return


    def make_trie(self,nums):
        _end = "_end_"
        root = dict()
        for num in nums:
            current_dict = root
            for letter in str(num):
                current_dict = current_dict.setdefault(letter, {})
            current_dict["_end"] = _end
        return root

sol = Solution()
nums = [12,32,432,56,357,9,98,789,69]

nums = [3, 30, 34, 5, 9]
nums = [121,12]
nums = [122,1222,1221,12,22,22]
#nums = [1,1,2,1,23,432,43,5,6,7,8,9,6,7,986]
nums = [4704,6306,9385,7536,3462,4798,5422,5529,8070,6241,9094,7846,663,6221,216,6758,8353,3650,3836,8183,3516,5909,6744,1548,5712,2281,3664,7100,6698,7321,4980,8937,3163,5784,3298,9890,1090,7605,1380,1147,1495,3699,9448,5208,9456,3846,3567,6856,2000,3575,7205,2697,5972,7471,1763,1143,1417,6038,2313,6554,9026,8107,9827,7982,9685,3905,8939,1048,282,7423,6327,2970,4453,5460,3399,9533,914,3932,192,3084,6806,273,4283,2060,5682,2,2362,4812,7032,810,2465,6511,213,2362,3021,2745,3636,6265,1518,8398]
nums = [22,2228,21,2221,222]
nums = [7543,5328,9834,1940,9387,871,5208,7,543]
nums = [7543 , 7 , 77]
res = sol.largestNumberII(nums)
a = res
b = "98909827968595339456944893859149094902689398937839883538183810810780707982784676057536747174237321720571007032685668066758674466986636554651163276306626562416221603859725909578457125682552954605422520849804812479847044453428339323905384638363699366436503636357535673516346233993298316330843021297028227452732697246523622362231322281216213206020001921763154815181495141713801147114310901048"
b = "98909827968595339456944893859149094902689398937839883538183810810780707982784676057536747174237321720571007032685668066758674466986636554651163276306626562416221603859725909578457125682552954605422520849804812479847044453428339323905384638363699366436503636357535673516346233993298316330843021297028227452732697246523622362231322812216213206020001921763154815181495141713801147114310901048"

print a == b
print res

