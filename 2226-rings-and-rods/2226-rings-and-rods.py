class Solution:
    def countPoints(self, rings: str) -> int:
        rods = {}
        for i in range(0,len(rings),2):
            colour = rings[i]
            rod = rings[i+1]

            if rod not in rods:
                rods[rod] = set()
            rods[rod].add(colour)
        
        count = 0
        for colour in rods.values():
            if {'R', 'G', 'B'}.issubset(colour):
                count += 1
        return count