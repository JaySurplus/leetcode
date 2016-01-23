"""
	87. Scramble String

	Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

	Below is one possible representation of s1 = "great":


	   great
   	  /    \
  	 gr    eat
 	/ \    /  \
	g   r  e   at
           	   / \
              a   t



	To scramble the string, we may choose any non-leaf node and swap its two children.

	For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".

        rgeat
       /    \
      rg    eat
     / \    /  \
	r   g  e   at
               / \
              a   t
	We say that "rgeat" is a scrambled string of "great".

	Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".

        rgtae
       /    \
      rg    tae
     /  \    /  \
	 r   g  ta  e
            / \
           t   a
	We say that "rgtae" is a scrambled string of "great".

	Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.


	https://leetcode.com/problems/scramble-string/





"""



class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        #for i in xrange(1,len(s2)):
        res = self.rotate(s1,s2) 
        #print res


    def rotate(self,s1,s2):
    	if len(s2) > 1:
    		for i in xrange(1,len(s2)): 

    			s21 = self.rotate(s1,s2[i:])+self.rotate(s1,s2[:i])
    			if s21 == s1:
    				print True
    			s22 = s2[i:] + self.rotate(s1,s2[:i])
    			if s22 == s1:
    				print True
    			s23 = self.rotate(s1,s2[:i]) + s2[i:]
    			if s23 == s1:
    				print True
    			s24 = self.rotate(s1,s2[:i]) + self.rotate(s1,s2[i:])
    			if s23 == s1:
    				print True
    	
    	return s2
    		





sol = Solution()
s1 = 'great'
s2 = 'rgeat'
print sol.isScramble(s1,s2)
print 