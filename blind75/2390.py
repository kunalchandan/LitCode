from typing import List


class Solution:
    def removeStars(self, s: str) -> str:
        stack: List[str] = []
        index = 0
        for _ in range(len(s)):
            if s[index] == "*":
                stack.pop()
            else:
                stack.append(s[index])
            index += 1
        return ''.join(stack)


print(Solution().removeStars("leet**cod*e"))
