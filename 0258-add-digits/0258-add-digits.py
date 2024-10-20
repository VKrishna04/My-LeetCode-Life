class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num)) != 1:
            num = sum(int(_) for _ in str(num))

        # while num > 9: num = sum(int(d) for d in str(num))
        return num