from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # max_alt = 0
        # alt = 0
        # for i, v in enumerate(gain):
        #     alt = alt + v
        #     max_alt = max(max_alt, alt)
        # return max_alt
        return max(max(sum(gain[:i+1]) for i in range(len(gain))), 0)

