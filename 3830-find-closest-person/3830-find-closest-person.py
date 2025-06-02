class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        a = abs(z - x) 
        b = abs(z - y)
        if b > a:
            return 1
        elif a > b:
            return 2
        else:
            return 0