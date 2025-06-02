class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums = set(nums)
        try:
            nums.remove(0)
        finally:
            return len(nums)
