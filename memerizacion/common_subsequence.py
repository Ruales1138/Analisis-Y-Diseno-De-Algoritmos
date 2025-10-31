def common_subsequence(string_1, string_2):
    memo = {}
    def dp(string_1, string_2, i=0, j=0):
        if f'{string_1[i:]} {string_2[j:]}' in memo:
            return memo[f'{string_1[i:]} {string_2[j:]}']
        if i == len(string_1) or j == len(string_2):
            return 0
        if string_1[i] == string_2[j]:
            memo[f'{string_1[i:]} {string_2[j:]}'] = 1 + dp(string_1, string_2, i+1, j+1)
            return memo[f'{string_1[i:]} {string_2[j:]}']
        else:
            memo[f'{string_1[i:]} {string_2[j:]}'] = max(dp(string_1, string_2, i+1, j), dp(string_1, string_2, i, j+1))
            return memo[f'{string_1[i:]} {string_2[j:]}']
    return dp(string_1, string_2)

print(common_subsequence('abcde', 'ace')) # -> 3 (“ace”)
print(common_subsequence('abc', 'def')) # -> 0