def coin_change(coins: list[int], amount: int) -> int:
    memo = {}
    def dp(coins, amount):
        if amount in memo:
            return memo[amount]
        memo[amount] = float('inf')
        for coin in coins:
            if amount - coin == 0:
                memo[amount] = 1
                return 1
            if amount - coin > 0:
                result = coin_change(coins, amount-coin) + 1 
                memo[amount] = min(result, memo[amount])
        return memo[amount]
    return dp(coins, amount)


print(coin_change([1,5], 3)) # ---> 3
print(coin_change([1,2,3], 5)) # ---> 2
print(coin_change([1,2,3], 3)) # ---> 1
print(coin_change([1,2,5], 11)) # ---> 3
print(coin_change([2], 3)) # ---> -1