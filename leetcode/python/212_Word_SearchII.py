git"""
    212. Word Search II


    Given a 2D board and a list of words from the dictionary, find all words in the board.

    Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

    For example,
    Given words = ["oath","pea","eat","rain"] and board =

    [
        ['o','a','a','n'],
        ['e','t','a','e'],
        ['i','h','k','r'],
        ['i','f','l','v']
    ]
    Return ["eat","oath"].

"""

class Trie(object):
    def __init__(self):
        pass

class Solution(object):
    def findWord(self, board, words):
        if not words or not board or not board[0]:
            return []

        lCharDic = {}
        lCharMaxLDic = {}

        for word in words:
            if word[0] not in lCharDic:
                lCharDic[word[0]] = []
            lCharDic[word[0]]+= [word]
            lCharMaxLDic[word[0]] = max(lCharMaxLDic.get(word[0]), len(word))
        print lCharDic,lCharMaxLDic

sol = Solution()
words = ["oath","pea","eat","rain" , "pee"]
board =[
        ['o','a','a','n'],
        ['e','t','a','e'],
        ['i','h','k','r'],
        ['i','f','l','v']
       ]


sol.findWord(board,words)
