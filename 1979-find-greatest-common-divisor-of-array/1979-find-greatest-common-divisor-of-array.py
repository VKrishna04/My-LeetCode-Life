class Solution:
    def findGCD(self, nums: List[int]) -> int:
        s = min(nums)
        l = max(nums)

        while (l != 0):
            s, l = l, s % l
        return s

        # Using built in functions
        # from math import gcd
        # return gcd(min(nums), max(nums))
