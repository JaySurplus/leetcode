"""
    408 Valid Word Abbreviation
"""

import re
class Solution(object):
        def validWordAbbreviation(self, word, abbr):
            return bool(re.match(re.sub('([1-9]\d*)', r'.{\1}', abbr) + '$', word))

sol = Solution()

