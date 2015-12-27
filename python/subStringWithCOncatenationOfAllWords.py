"""
	Substring with Concatenation of All Words

	You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

	For example, given:
		s: "barfoothefoobarman"
		words: ["foo", "bar"]

	You should return the indices: [0,9].


"""
import copy
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        lenWs = len(words) * len(words[0])
        lenS = len(s)
        lenW = len(words[0])
        nW = len(words)


        result = []
        index = []
       	first_init = []
       	dic = {}


       	for i in words:
       		if i[0] not in first_init:
       			first_init.append(i[0])
     		if i not in dic.keys():
     			dic[i] = 1
     		else:
     			dic[i] += 1

     
       	for i in range(lenS-lenWs+1):
       		if s[i] in first_init:
       			index.append(i)		
    	

        for i in index:
       		temp = {}
       		j = 0
        	while j < nW:
        		curr = s[i+lenW*j:i+lenW*(j+1)]
        		if curr not in dic:
        			break
        		if curr not in temp:
        				temp[curr] = 1
        		else:
        			temp[curr] += 1
        		if temp[curr] > dic[curr]:
        			break 	
        		j += 1
        	if j == nW:
        		result.append(i)
        
        return result
        

        
sol = Solution()
s = "wordgoodgoodgoodbestword"
words = ["word","good","best","good"]


print sol.findSubstring(s,words)