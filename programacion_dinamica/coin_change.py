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
                resultado = dp(coins, amount - coin)
                resultado += 1
                memo[amount] = min(resultado, memo[amount])
            else:
                return float('inf')
        return memo[amount]
    dp(coins, amount)
    return memo[amount]


print(coin_change([1,2,3], 5)) # ---> 2
print(coin_change([1,2,3], 3)) # ---> 1
print(coin_change([1,2,5], 11)) # ---> 3
print(coin_change([2], 3)) # ---> -1