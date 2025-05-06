class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        s1 = Counter(ransomNote)
        s2 = Counter(magazine)
        if s1 & s2 == s1:
            return True
        return False