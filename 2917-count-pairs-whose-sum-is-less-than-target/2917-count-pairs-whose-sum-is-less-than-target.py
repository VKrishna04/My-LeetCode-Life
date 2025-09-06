class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0
        nums.sort()
        ans = 0
        for l in range(len(nums)-1):
            for r in range(l+1,len(nums)):
                if nums[l]+nums[r]<target:
                    ans += 1
                    print(f"{nums[l]}, {nums[r]}")
        return ans