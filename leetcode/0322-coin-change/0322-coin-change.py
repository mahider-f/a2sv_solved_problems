class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(amount):
            if amount == 0:
                return 0
            if amount in memo:
                return memo[amount]
            res = float('inf')
            for coin in coins:
                if amount - coin >= 0:
                    res = min(res,dfs(amount - coin) + 1)
            memo[amount] = res
            return res
        ans = dfs(amount)

        if ans > amount:
            return -1
        return ans
            