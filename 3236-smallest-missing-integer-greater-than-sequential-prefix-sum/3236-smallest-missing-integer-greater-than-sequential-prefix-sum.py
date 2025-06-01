class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                sum += nums[i]
            else:
                break
        while sum in nums:
            sum += 1

        return sum
