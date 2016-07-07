"""
    211. Add and Search Word - Data structure design
"""


class WordDictionary(object):
    def __init__(self):
        self.word_dict = collections.defaultdict(list)


    def addWord(self, word):
        if word:
            self.word_dict[len(word)].append(word)

    def search(self, word):
        if not word:
            return False
        if '.' not in word:
            return word in self.word_dict[len(word)]
        for v in self.word_dict[len(word)]:
            # match xx.xx.x with yyyyyyy
            for i, ch in enumerate(word):
                if ch != v[i] and ch != '.':
                    break
            else:
                return True
        return False


"""
#!/usr/bin/python

class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.dic = {"end": True}
        self.added = {}


    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        def recursiveAdd(w,dic):
            if not w and "end" not in dic:
                dic["end"] = True
            else:
                if w[0] in dic:
                    recursiveAdd(w[1:],dic[w[0]])
                else:
                    dic[w[0]] = {}
                    recursiveAdd(w[1:],dic[w[0]])
        if word not in self.added:
            recursiveAdd(word,self.dic)
            self.added[word] = True





    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        def recursiveSearch(w,dic):

            if not w:
                return "end" in dic
            else:
                if w[0] in dic:
                    return recursiveSearch(w[1:] , dic[w[0]])
                else:
                    if w[0] != '.':
                        return False
                    else:
                        for k in dic:
                            if k == "end":
                                continue
                            temp = recursiveSearch(w[1:] , dic[k])
                            if temp == True:
                                return True
                        return False


        if word in self.added:
            return True
        elif len(word.split(".")) == 1:

            return False
        else:
            return recursiveSearch(word,self.dic)
"""
