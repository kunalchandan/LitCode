class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        ret = ""
        for i in range(min(len(str1), len(str2))):
            divisor = str1[:i+1]
            if (divisor * max(len(str1)//len(divisor), 1) == str1) and \
                    (divisor * max(len(str2)//len(divisor), 1) == str2):
                ret = divisor
        return ret
