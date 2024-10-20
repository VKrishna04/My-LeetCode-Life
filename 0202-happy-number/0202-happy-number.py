class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = sum(int(_) ** 2 for _ in str(n))

        # while n > 9: n = sum(int(d) ** 2 for d in str(n))
        if n == 1:
            return True
        return False