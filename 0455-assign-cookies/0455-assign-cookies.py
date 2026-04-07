class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        l = 0
        r = 0
        g.sort()
        s.sort()

        while l < len(s) and r < len(g):
            if g[r] <= s[l]:
                r += 1
            l += 1
        
        return r