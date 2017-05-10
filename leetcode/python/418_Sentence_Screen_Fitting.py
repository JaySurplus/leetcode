"""
    418. Sentence Screen Fitting
    Given a rows x cols screen and a sentence represented by a list of non-empty words, find how many times the given sentence can be fitted on the screen.

    Note:

        A word cannot be split into two lines.
        The order of words in the sentence must remain unchanged.
        Two consecutive words in a line must be separated by a single space.
        Total words in the sentence won't exceed 100.
        Length of each word is greater than 0 and won't exceed 10.
        1 ≤ rows, cols ≤ 20,000.
        example 1:

        input:
        rows = 2, cols = 8, sentence = ["hello", "world"]

        output:
        1

        explanation:
        hello---
        world---

        the character '-' signifies an empty space on the screen.
        example 2:

        input:
        rows = 3, cols = 6, sentence = ["a", "bcd", "e"]

        output:
        2

        explanation:
        a-bcd-
        e-a---
        bcd-e-

        the character '-' signifies an empty space on the screen.
        example 3:

        input:
        rows = 4, cols = 5, sentence = ["i", "had", "apple", "pie"]

        output:
        1

        explanation:
        i-had
        apple
        pie-i
        had--

        the character '-' signifies an empty space on the screen.
"""
class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """






