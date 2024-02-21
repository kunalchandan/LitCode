from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Timeout :(
        return max([max([(min(h1, h2) * j) for j, h2 in enumerate(height[i:])]) for i, h1 in enumerate(height)])
        # Timeout :(
        # max_vol = 0
        # for i, h in enumerate(height):
        #     for j, h2 in enumerate(height[i:]):
        #         vol = min(h, h2) * (j)
        #         max_vol = max(vol, max_vol)
        # return max_vol
