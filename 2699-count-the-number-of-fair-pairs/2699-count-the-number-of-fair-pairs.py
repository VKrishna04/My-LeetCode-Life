from bisect import bisect_left, bisect_right
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        # if len(nums) == 1:
        #     return 0
        # nums.sort()
        # ans = 0
        # for l in range(len(nums)-1):
        #     for r in range(l+1,len(nums)):
        #         if lower<=(nums[l]+nums[r])<=upper:
        #             ans += 1
        #             print(f"{nums[l]}, {nums[r]}")
        # return ans

        nums.sort()
        count = 0
        for i in range(len(nums)):
            left = bisect_left(nums, lower - nums[i], i+1)
            right = bisect_right(nums, upper - nums[i], i+1)
            count += right - left
        return count