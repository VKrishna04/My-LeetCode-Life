class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]
        for i in range(len(nums)):
            if nums[0] > nums[i]:
                               
                return nums[i]
