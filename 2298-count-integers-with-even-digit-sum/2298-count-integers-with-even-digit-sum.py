class Solution:
    def countEven(self, num: int) -> int:
        output = 0
        for i in range(1, num+1):
            digits = list(map(int, str(i)))
            if sum(digits) % 2 == 0:
                output += 1

        return output