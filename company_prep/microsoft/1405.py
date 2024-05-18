"""
1405. Longest Happy String
A string s is called happy if it satisfies the following conditions:
    s only contains the letters 'a', 'b', and 'c'.
    s does not contain any of "aaa", "bbb", or "ccc" as a substring.
    s contains at most a occurrences of the letter 'a'.
    s contains at most b occurrences of the letter 'b'.
    s contains at most c occurrences of the letter 'c'.
Given three integers a, b, and c, return the longest possible happy string.
    If there are multiple longest happy strings, return any of them.
    If there is no such string, return the empty string "".
Example 1:
    Input: a = 1, b = 1, c = 7
    Output: "ccaccbcc"
    Explanation: "ccbccacc" would also be a correct answer.
Example 2:
    Input: a = 7, b = 1, c = 0
    Output: "aabaa"
    Explanation: It is the only correct answer in this case.
Constraints:
    0 <= a, b, c <= 100
    a + b + c > 0
"""
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        accumulator = ""
        letters = [['a', a], ['b', b], ['c', c]]
        largest = sorted(letters, key=lambda x: x[1], reverse=True)
        print(largest)
        max_repeat = 2
        can_generate = True
        counter_max = sum([pair[1] for pair in largest])
        counter = 0
        while can_generate and counter < counter_max:
            for ii in range(max_repeat):
                for jj, pair in enumerate(largest):
                    if pair[1] > 0:
                        if (len(accumulator) >= 2 and any(pair[0] != acc for acc in accumulator[-max_repeat:])) or len(accumulator) < 2:
                            accumulator += pair[0]
                            print(accumulator)
                            pair[1] -= 1
                            break
                    else:
                        pass
                largest = sorted(largest, key=lambda x: x[1], reverse=True)
            largest = sorted(largest, key=lambda x: x[1], reverse=True)
            # pop = largest.pop(0)
            # largest.append(pop)
            counter += 1
            can_generate = sum([pair[1] for pair in largest]) > 0
        return accumulator


    def longestDiverseString2(self, a: int, b: int, c: int) -> str:
        accumulator = ""
        ct = 0
        largest = max([a, b, c])
        while a + b + c > 0:
            if ct % 3 == 0:

                pass
            elif ct % 3 == 1:
                pass
            else:
                pass
            ct += 1
        return ""



import unittest

def eval_string(string: str) -> bool:
    if any(double in string for double in ['aaa', 'bbb', 'ccc']):
        return False
    return True

class TestFN(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_01(self):
        solution = self.solution.longestDiverseString(1, 2, 3)
        self.assertTrue(eval_string(solution))
        self.assertEqual(solution, 'ccbbca')

    def test_02(self):
        solution = self.solution.longestDiverseString(1, 1, 7)
        self.assertTrue(eval_string(solution))
        self.assertEqual(solution, 'ccbccacc')
