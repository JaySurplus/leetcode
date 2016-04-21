"""
	68. Text Justification

	https://leetcode.com/problems/text-justification/


	Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.

	You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.

	Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

	For the last line of text, it should be left justified and no extra space is inserted between words.

	For example,
		words: ["This", "is", "an", "example", "of", "text", "justification."]
	L: 16.

	Return the formatted lines as:
	[
   		"This    is    an",
   		"example  of text",
   		"justification.  "
	]
"""

class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        temp = [words[0]]
        count = len(words[0])
        res = []
        i = 1
        while i < len(words) :
      
        	if (maxWidth - count - len(words[i]))/len(temp) >= 1:
        		count += len(words[i])
        		temp.append(words[i])
        		i += 1

        	else:
        	
        		if len(temp) == 1:
        			res.append(temp[0]+' '*(maxWidth-count))
        			
        		else:
        			ave = (maxWidth - count)/(len(temp)-1)
        			ext = (maxWidth - count)%(len(temp)-1)
        			tempStr = temp[0]
        			for k in range(1, len(temp)):
        				tempStr+= ' '*ave
        				if ext != 0:
        					tempStr+= ' '
        					ext -= 1
        				tempStr+= temp[k]
        			res.append(tempStr)

        		temp = [words[i]]
        		count = len(words[i])
        		i += 1

       	if len(temp) != 0:
       		tempStr = ' '.join(temp)
       		tempStr += ' '* (maxWidth - len(tempStr))
       		res.append(tempStr)
		      
        return res

sol = Solution()
words = ["This", "is", "an", "example", "of", "text", "justification." ,"haa" , "haha" ]
maxWidth = 17
result = sol.fullJustify(words,maxWidth)

for i in range(len(result)):
	print result[i]

