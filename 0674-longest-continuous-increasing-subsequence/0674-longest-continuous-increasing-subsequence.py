class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        best = count = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                count += 1
            else:
                count = 1
            
            best = max(best, count)
        return best