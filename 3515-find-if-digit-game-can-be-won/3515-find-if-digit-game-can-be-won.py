class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single = 0
        double = 0
        for num in nums:
            if len(str(num)) == 2:
                double += num
            else:
                single += num

        if single == double:
            return False
        return True