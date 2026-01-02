class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = ans = nums[0]

        for x in nums[1:]:
            curr = max(x, curr + x)
            ans = max(ans, curr)
        return ans