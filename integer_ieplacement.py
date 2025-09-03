def integer_ieplacement(n):
    memo = {2:1, 1:0}
    def dp(n):
        if n in memo:
            return memo[n]
        if n % 2 == 0:
            memo[n] = 1 + integer_ieplacement(int(n/2))
        else:
            memo[n] = min( (1 + integer_ieplacement(int(n-1))), (1 + integer_ieplacement(int(n+1))) )
        return memo[n]
    return dp(n)

print(integer_ieplacement(8))