class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev = 0
        curr = 0
        for i in range(2, len(cost) + 1):
            prev , curr = curr, min(prev + cost[i-2], curr + cost[i-1])
        return curr