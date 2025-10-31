def decode_ways(string):
    memo = {}
    n = len(string)
    def dp(string, n, i=0):
        if i in memo:
            return memo[i]
        if i == n:
            return 1
        if string[i] == '0':
            return 0
        ways = dp(string, n, i+1)
        if i+1 < n and 10 <= int(string[i:i+2]) <= 26 :
            ways += dp(string, n, i+2)
        memo[i] = ways
        return ways
    return dp(string, n)

print(decode_ways('12')) # -> 2 (“AB”, “L”)
print(decode_ways('226')) # -> 3 (“BBF”, “BZ”, “VF”)
print(decode_ways('06')) # -> 0
print(decode_ways('4521')) # -> 2 ('DEBA', 'DEU')