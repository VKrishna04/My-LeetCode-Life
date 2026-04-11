class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n, s = len(colors), 0
        for i in range(1, n):
            if colors[i] == colors[i - 1]:
                s += min(neededTime[i], neededTime[i - 1])
                neededTime[i] = max(neededTime[i], neededTime[i-1])
        return s 