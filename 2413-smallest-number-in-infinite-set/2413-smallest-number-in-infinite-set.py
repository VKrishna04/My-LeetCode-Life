class SmallestInfiniteSet:

    def __init__(self):
        self.sm = 1
        self.rm = set()

    def popSmallest(self) -> int:
        ans = self.sm
        self.rm.add(ans)
        while self.sm in self.rm:
            self.sm += 1
        return ans

    def addBack(self, num: int) -> None:
        if num in self.rm:
            self.rm.remove(num)
            if num < self.sm:
                self.sm = num


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)