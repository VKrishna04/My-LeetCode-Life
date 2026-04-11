class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        n = len(s)
        if n == 1:
            return 1
        
        prev = 1
        curr = 1

        for i in range(2, n+1):
            temp = 0
            if int(s[i-1:i]) > 0:
                temp += curr
            if 10 <= int(s[i-2:i]) <= 26:
                temp += prev
            prev, curr = curr, temp
        return curr