class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        ans = []

        for i in range(int(len(nums)/2)):
            ans.append(nums[i]+nums[len(nums)-i-1])
        
        return max(ans)