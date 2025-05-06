class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip().split(" ")
        l = s[-1]
        return len(l)