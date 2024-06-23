def minDist(w1, w2):
    l1, l2 = len(w1) + 1, len(w2) + 1
    dp = []
    for i in range(l1):
        dp.append([0] * l2)
    for i in range(l1):  
        dp[i][0] = i
    for j in range(l2):  
        dp[0][j] = j
    for i in range(1, l1):
        for j in range(1, l2):
            dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1,dp[i-1][j-1]+ (w1[i-1] != w2[j-1]))
    return dp[-1][-1]
print(minDist("intention","execution"))