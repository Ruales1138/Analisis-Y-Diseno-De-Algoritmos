def sum_coins(coins, amount):
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

print(sum_coins([100,15,20], 50))
print(sum_coins([1], 200))