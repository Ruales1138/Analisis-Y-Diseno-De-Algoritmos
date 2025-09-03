def coin_change(coins: list[int], amount: int) -> int:
    memo = {amount: float('inf')}
    def dp(coins, amount):
        #print(amount)
        for coin in coins:
            if amount - coin < 0:
                return float('inf')
            if amount - coin == 0:
                return 0
            else:
                resultado = 1 + dp(coins, amount - coin)
                print(resultado)
                memo[amount] = min(resultado, memo[amount])
    dp(coins, amount)
    return memo[amount]


print(coin_change([1,2,3], 5)) # ---> 2
print()
print(coin_change([1,2,3], 3)) # ---> 1
# print()
# print(coin_change([1,2,5], 11)) # ---> 3
# print()
# print(coin_change([2], 3)) # ---> -1