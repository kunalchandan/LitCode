from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        return max(max(sum(gain[:i+1]) for i in range(len(gain))), 0)

