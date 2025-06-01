class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n >= 3:
            # print(n)
            n /= 3
        # print(n)
        if n != 1:
            return False
        return True