class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        for k in range(len(nums)-2):
            if k > 0 and nums[k] == nums[k-1]:
                continue
            target = -nums[k]

            i = k+1
            j = len(nums) - 1

            while i < j:
                if nums[i] + nums[j] < target:
                    i += 1
                
                elif nums[i] + nums[j] > target:
                    j -= 1
                
                else:
                    ans.append([nums[k], nums[i], nums[j]])

                    while i < j and nums[i] == nums[i+1]:
                        i += 1
                    while i < j and nums[j] == nums[j-1]:
                        j -= 1
                    i += 1
                    j -= 1
        return ans