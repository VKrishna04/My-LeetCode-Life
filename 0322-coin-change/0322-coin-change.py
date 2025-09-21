class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for curr_amt in range(1,amount+1):
            for coin in coins:
                if curr_amt - coin >= 0 and dp[curr_amt - coin] != float('inf'):
                    dp[curr_amt] = min(dp[curr_amt], 1 + dp[curr_amt - coin])
        
        if dp[amount] == float('inf'):
            return -1
        else:
            return dp[amount]

        # if amount == 0:
        #     return 0
        # count = 0
        # coins.sort(reverse=True)

        # for i in coins:
        #     print(f"coin -> {i}")
        #     while i <= amount:
        #         count += 1
        #         print(f"  amount -> {amount}, new amount -> {amount - i}")
        #         amount -= i
        # if count == 0 or amount != 0:
        #     return -1
        # return count