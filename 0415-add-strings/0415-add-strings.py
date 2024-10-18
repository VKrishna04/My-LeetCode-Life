class Solution:
    def addStrings(self, a: str, b: str) -> str:
        if len(b) > len(a):
            a, b = b, a
        
        carry = 0
        result = []
        a = list(a)[::-1]
        b = list(b)[::-1]

        for i in range(len(a)):
            bit_a = int(a[i])
            bit_b = int(b[i]) if i < len(b) else 0
            total = bit_a + bit_b + int(carry)
            result.append(str(total % 10))
            carry = total // 10

        if carry:
            result.append(str(carry))

        return "".join(result[::-1])