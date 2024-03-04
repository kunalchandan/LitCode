from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # a + b = target
        # b = target - a
        bs = {(target - a): i for i, a in enumerate(nums)}
        for i, a in enumerate(nums):
            if a in bs and i != bs[a]:
                return [bs[a], i]

        return [0, 1]

    def twoSumSlow(self, nums: List[int], target: int) -> List[int]:
        for ii, a in enumerate(nums):
            for jj, b in enumerate(nums[ii+1:]):
                if a+b == target:
                    return [ii, ii+1+jj]
        return [0, 1]
