class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = len(nums)
        exs = s * ( s + 1) // 2
        return exs - sum ( nums )