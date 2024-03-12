from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window = nums[:k]
        avg = sum(window)/k
        avg_max = avg
        for i, v in enumerate(nums[:-k]):
            print(nums[i:1+i+k])
            avg = avg - (v/k)
            avg = avg + (nums[i+k]/k)
            avg_max = max(avg, avg_max)
        return avg_max


print(Solution().findMaxAverage([1, 12, -5, -6, 50, 3], 4))
