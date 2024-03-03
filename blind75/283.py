from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = 0
        for i in range(len(nums)):
            print(index)
            if nums[index] == 0:
                nums.pop(index)
                nums.append(0)
            else:
                index += 1


Solution().moveZeroes([0, 1, 0, 3, 12])
