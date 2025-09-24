def coin_change(coins, amount):
    coins.sort(reverse=True)
    def sum(coins, amount, i=0):
        if i == len(coins):
            return float('inf')
        coin = coins[i]
        if amount - coin == 0:
            return 1
        if amount - coin > 0:
            return 1 + sum(coins, amount-coin, i)
        else:
            return sum(coins, amount, i+1)
    return sum(coins, amount)

print(coin_change([100,15,20], 50))
print(coin_change([1], 200))