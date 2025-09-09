class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = 0
        sorted(nums)
        for i in range(len(nums)):
            count += len([j for j in range(len(nums)) if (nums[i]-k)==nums[j]])
        return count