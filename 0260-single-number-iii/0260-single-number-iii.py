class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        key_items = []
        frequency = {}
        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 0
        print(frequency)
        for key, value in frequency.items():
            if value == 0:
                key_items.append(key)
        return key_items