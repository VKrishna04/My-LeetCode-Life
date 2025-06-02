class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        return  sum(i.count('1') * i.count('0') for i in zip(*map('{:032b}'.format,nums)))
