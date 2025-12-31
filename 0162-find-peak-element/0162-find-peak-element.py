class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # Linear
        
        # for i in range(len(nums)):
        #     if (i==0 or (nums[i] > nums[i-1])) and (i == len(nums)-1 or (nums[i] > nums[i+1])):
        #         return i

        # O(log n) Binar Search

        n = len(nums)

        if n == 1 or nums[0] > nums[1]:
            return 0
        
        if nums[-1] > nums[-2]:
            return n-1

        low = 1
        high = n-2
        
        while low < high:
            mid = (low+high)//2

            if nums[mid] < nums[mid+1]:
                low = mid + 1
            else:
                high = mid
        return low
        
        