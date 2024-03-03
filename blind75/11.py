from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Timeout :(
        # return max([max([(min(h1, h2) * j) for j, h2 in enumerate(height[i:])]) for i, h1 in enumerate(height)])
        # Timeout :(
        # max_vol = 0
        # for i, h in enumerate(height):
        #     for j, h2 in enumerate(height[i:]):
        #         vol = min(h, h2) * (j)
        #         max_vol = max(vol, max_vol)
        # return max_vol
        a = 0
        b = len(height) - 1
        max_vol = 0
        while a < b:
            vol = min(height[a], height[b]) * (b-a)
            max_vol = max(max_vol, vol)
            if height[a] < height[b]:
                a += 1
            else:
                b -= 1

        return max_vol


print(Solution().maxArea([2, 3, 4, 5, 18, 17, 6]))
