class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d = {}
        for char in s:
            if char not in d:
                d[char] = 0
            d[char] += 1
        
        val = d[s[0]]
        for value in d.values():
            if value != val:
                return False
        return True