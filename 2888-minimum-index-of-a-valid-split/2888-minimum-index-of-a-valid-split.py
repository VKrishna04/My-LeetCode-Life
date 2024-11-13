class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        def count_elements(nums):
            counter = {}
            for num in nums:
                if num in counter:
                    counter[num] += 1
                else:
                    counter[num] = 1
            return counter

        full_counter = count_elements(nums)
        dominant_element = max(full_counter, key=full_counter.get)
        
        dominant_count = full_counter[dominant_element]
        
        left_count = 0
        for i in range(len(nums)):
            if nums[i] == dominant_element:
                left_count += 1
            right_count = dominant_count - left_count
            
            if left_count > (i + 1) // 2 and right_count > (len(nums) - i - 1) // 2:
                return i
        return -1
