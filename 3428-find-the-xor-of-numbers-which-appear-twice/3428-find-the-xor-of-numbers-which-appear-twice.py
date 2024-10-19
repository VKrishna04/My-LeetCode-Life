from functools import reduce
class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        frequency = {}
        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 0
        result = 0
        for key, value in frequency.items():
            if value == 1:
                result = result ^ key
        return result