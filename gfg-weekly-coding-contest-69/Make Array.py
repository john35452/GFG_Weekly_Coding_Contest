import sys
sys.setrecursionlimit(1000000)
class Solution:
    # Version 1: Top down DP
    # TC: O(n * K * 2) = O(nK), SC: O(n * K * 2)
    '''
    def makeArray(self, S : str, NUM : int, K : int) -> int:
        # code here
        def pick(index, tf, f, dp):
            if tf > K:
                return 0
            if index < 0:
                if tf == K:
                    return 1
                else:
                    return 0
            if dp[index][tf][f] != -1:
                return dp[index][tf][f]
            res = pick(index - 1, tf + f, f, dp)
            if val[index] == 0:
                res = (res + pick(index - 1, tf + (f^1), f^1, dp)) % M
            dp[index][tf][f] = res
            return dp[index][tf][f]
            
        n = len(S)
        M = 10**9 + 7
        val = [0]*(n + 1)
        base = 1
        for i in range(n - 1, -1, -1):
            val[i] = (val[i + 1] + int(S[i]) * base) % NUM
            base = (10 * base) % NUM

        dp = [[[-1]*2 for i in range(K + 1)] for _ in range(n)]
        ans = pick(n - 1, 0, 0, dp)
        return ans
    '''
    
    # Version 2: Bottom up DP
    # TC: O(nk), SC: O(nk)
    '''
    def makeArray(self, S : str, NUM : int, K : int) -> int:
        # code here
        n = len(S)
        M = 10**9 + 7
        val = [0]*(n + 1)
        base = 1
        for i in range(n - 1, -1, -1):
            val[i] = (val[i + 1] + int(S[i]) * base) % NUM
            base = (10 * base) % NUM

        dp = [[[0]*2 for i in range(K + 1)] for _ in range(n + 1)]
        dp[n][0][0] = 1
        for i in range(n - 1, -1, -1):
            dp[i][0][0] = dp[i + 1][0][0]
            dp[i][0][1] = dp[i + 1][0][1]
            for j in range(1, K + 1):
                dp[i][j][0] = dp[i + 1][j][0]
                dp[i][j][1] = dp[i + 1][j - 1][1]
                if val[i] == 0:
                    dp[i][j][0] += dp[i + 1][j][1]
                    dp[i][j][1] += dp[i + 1][j - 1][0]
                dp[i][j][0] %= M
                dp[i][j][1] %= M
        return (dp[0][K][0] + dp[0][K][1]) % M
    '''
    
    # Version 3: Improved version 2
    # TC: O(nk), SC: O(n + k)
    def makeArray(self, S : str, NUM : int, K : int) -> int:
        # code here
        n = len(S)
        M = 10**9 + 7
        val = [0]*(n + 1)
        base = 1
        for i in range(n - 1, -1, -1):
            val[i] = (val[i + 1] + int(S[i]) * base) % NUM
            base = (10 * base) % NUM
        
        dp = [[0]*2 for i in range(K + 1)]
        nextDp = [[0]*2 for i in range(K + 1)]
        dp[0][0] = 1
        for i in range(n - 1, -1, -1):
            nextDp[0][0] = dp[0][0]
            nextDp[0][1] = dp[0][1]
            for j in range(1, K + 1):
                nextDp[j][0] = dp[j][0]
                nextDp[j][1] = dp[j - 1][1]
                if val[i] == 0:
                    nextDp[j][0] += dp[j][1]
                    nextDp[j][1] += dp[j - 1][0]
                nextDp[j][0] %= M
                nextDp[j][1] %= M
            dp, nextDp = nextDp, dp
        return (dp[K][0] + dp[K][1]) % M
