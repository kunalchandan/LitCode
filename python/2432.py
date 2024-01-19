"""
2423. Remove Letter To Equalize Frequency
You are given a 0-indexed string word, consisting of lowercase English letters.
You need to select one index and remove the letter at that index from word so that the
frequency of every letter present in word is equal.
Return true if it is possible to remove one letter so that the frequency of all letters in word are equal, and false otherwise.
Note:
    The frequency of a letter x is the number of times it occurs in the string.
    You must remove exactly one letter and cannot choose to do nothing.
Example 1:
    Input: word = "abcc"
    Output: true
    Explanation: Select index 3 and delete it: word becomes "abc" and each character has a frequency of 1.
Example 2:
    Input: word = "aazz"
    Output: false
    Explanation: We must delete a character, so either the frequency of "a" is 1 and the frequency of "z" is 2, or vice versa. It is impossible to make all present letters have equal frequency.

Constraints:
    2 <= word.length <= 100
    word consists of lowercase English letters only.
"""


class Solution:
    def equalFrequency(self, word: str) -> bool:
        counts = dict()
        for letter in word:
            counts[ord(letter)] = counts.get(ord(letter), 0) + 1
        count_nums = sorted(list(counts.values()))
        if len(set(count_nums)) >= 3:
            return False
        else:
            lcn = len(count_nums)
            cn2d = [count_nums for i in range(lcn)]
            # Remove one letter for each
            cn2d = [[cn2d[jj][ii]-1 if ii == jj else cn2d[jj][ii] for ii in range(lcn)] for jj in range(lcn)]
            cn2d = [list(filter(lambda x: x != 0, cn)) for cn in cn2d] # Filter deletions
            truthy = [(cn.count(cn[0]) == len(cn)) for cn in cn2d]
            return True if any(truthy) else False

    def equalFrequency2(self, word: str) -> bool:
        counts = dict()
        for letter in word:
            counts[ord(letter)] = counts.get(ord(letter), 0) + 1
        max_n = max(counts.values())
        min_n = min(counts.values())
        if (min_n == 1) and list(counts.values()).count(min_n) == 1:
            return True
        elif len(counts.values()) == 1:
            return True
        elif (min_n == max_n) and (min_n == 1):
            return True
        elif max_n == min_n:
            return False
        elif (max_n - min_n) >= 2:
            return False
        else:
            # May have multiple maxs
            if list(counts.values()).count(max_n) > 1:
                return False
            else:
                return True

    def equalFrequencyFAIL(self, word: str) -> bool:
        counts = [
            0,
        ] * 26
        for i, letter in enumerate(word):
            counts[ord(letter) - 97] += 1
        max_n = max(counts)
        min_n = min(counts)
        if ((max_n - min_n) == 0) or ((max_n - min_n) >= 2):
            return False
        else:
            # May have multiple maxs
            if counts.count(max_n) > 1:
                return False
            else:
                return True


import unittest


class TestFN(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_01(self):
        self.assertEqual(self.solution.equalFrequency("abcc"), True)

    def test_02(self):
        self.assertEqual(self.solution.equalFrequency("aazz"), False)

    def test_03(self):
        self.assertEqual(self.solution.equalFrequency("abbcc"), True)

    def test_04(self):
        self.assertEqual(self.solution.equalFrequency("aaaaa"), True)

    def test_05(self):
        self.assertEqual(self.solution.equalFrequency("aaabb"), True)

    def test_06(self):
        self.assertEqual(self.solution.equalFrequency("bbbacc"), False)

    def test_07(self):
        self.assertEqual(self.solution.equalFrequency("babbdd"), False)
