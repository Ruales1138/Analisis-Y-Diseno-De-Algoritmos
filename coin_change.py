def coin_change(coins: list[int], amount: int) -> int:
    memo = {}
    def dp(coins, amount, current = 0, count = 0, ways = []):
        for coin in coins:
            if coin + current == amount:
                current += coin
                ways.append(count)
            if coin + current < amount:
                current += coin
                count += 1
                dp(coins, amount, current, count, ways)
                current -= coin
                count -= 1
        if ways == []:
            return -1
        else:
            #return ways
            return min(ways)
    return dp(coins, amount)


print(coin_change([1,2,3], 1)) # ---> 1
print()
print(coin_change([1,2,3], 3)) # ---> 1
print()
print(coin_change([1,2,5], 11)) # ---> 3
print()
print(coin_change([2], 3)) # ---> -1