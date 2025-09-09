def decode_ways(string):
    memo = {}
    def dp(string, i=0):
        if i == len(string):
            return 1
        if string[i] == '0':
            return 0
        return dp(string, i+1)
    return dp(string)

print(decode_ways('12')) # -> 2 (“AB”, “L”)
print(decode_ways('226')) # -> 3 (“BBF”, “BZ”, “VF”)
print(decode_ways('06')) # -> 0
print(decode_ways('4521')) # -> 2 ('DEBA', 'DEU')