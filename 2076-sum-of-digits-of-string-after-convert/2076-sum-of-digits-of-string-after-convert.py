class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num = int(''.join(str(ord(c) - ord('a') + 1) for c in s))
        for i in range(k):
            num = sum(int(digit) for digit in str(num))
        return num