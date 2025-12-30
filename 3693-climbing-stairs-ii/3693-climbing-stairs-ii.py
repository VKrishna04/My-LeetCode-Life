class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        back1 = back2 = back3 = 0

        for stepCost in costs:
            minCost = min(back1 + 1, back2 + 4, back3 + 9)

            back1, back2, back3 = stepCost + minCost, back1, back2
        
        return back1