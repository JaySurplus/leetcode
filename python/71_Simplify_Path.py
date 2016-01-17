"""
	71. Simplify Path

	https://leetcode.com/problems/simplify-path/

	Given an absolute path for a file (Unix-style), simplify it.

	For example,
	path = "/home/", => "/home"
	path = "/a/./b/../../c/", => "/c"

"""

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        
        stack = []
        
        i = 0
        while i < len(path):
        	j = i
        	while j < len(path) and path[j] != '/':
        		j+=1
        	temp = path[i:j]
        	i = j + 1
        	if temp == '..' or temp == '.' or temp == '':
        		if temp == '..' and len(stack) > 0:  
        			stack.pop()
        	else:
        		stack.append(temp)
        return '/'+'/'.join(stack)
    

    def simplifyPathII(self, path):
        stack = []
        for item in path.split("/"):

        	if item not in [".", "..", ""]:
        		stack.append(item)
        	if item == ".." and stack:
        		stack.pop()
        return "/" + "/".join(stack)

sol = Solution()
path =  "/home/"
path = "/a/./b/..////../c"
#path = "/./fdasfas/"
#path = "/WXSLrhBRvusul/cWW/uEQgMDoYroKdIh/KoYviLpPCPPimFzlMYVT///MqvEfpurzHSSGSa/./././gkSGICoP///QoRYl/K/////mCcX/../fE///rKqxjILfsTF/LHvBqzl/./jmnXGKEdxkSTNsM/////A///./fDbjTMxtaeoOiexI/./zJMNZvEk///EeILv/DPQGJfKfK/./J/../oNQAMeiJsbuwZclYmJG///././TUFFTIXEaThTqfkqF/GbEyDbz/..///../UQJdzIJDdwT/././XzxJYUEAlpzT/OiDwsVTxuSScaBTyOeDf///////./HkvhGJSfJubqDSeNXVPy/oBfA/.././wrn/RNvuIKmGIQKfoPUWSm/wZxokEDZTuzShaslvy/ZLkrJlXaJozvU/CY/z/zhs///./ZSIZ/wCRxGuPPMGfiwFu/////.././zlZMNl/bYoJUseKepDxhDvamJw/wIJ/pZLiCTEEKhvKufQnLw/../../../RpyIlDHjHS/////dXARt/pj/.././CCCWZNzepbDONRE/uYsbPOXkeXFUmEBI/azZ/iKzVehBGAbZ/fQkuSugIiB/.///../////bzeZfQg/./../LHnSqbynpcF/NDrdvakcdCEcR/////NAoacdhiaW/../OjNNxI/..///..///G/////./.././//./../CflNCUm/../../PZxxkBfleyePRoahJxoe/VkLVJnxCkRMbQZL/////tl/qNKJUjtzFPmLUYXNCz/."
#path = "/....."
print sol.simplifyPath(path)