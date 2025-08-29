def coin_change(coins: list[int], amount: int) -> int:
    memo: dict = {}
    def dp(coins, amount, current: int = 0, i: int = 0):
        if coins[i] + current < amount:
            current += coins[i]
            print(current)
            return dp(coins, amount, current, i)
    return dp(coins, amount)

print(coin_change([1,2,3], 3)) # ---> 3
print()
print(coin_change([1,2,5], 11)) # ---> 3
print(coin_change([2], 3)) # ---> -1