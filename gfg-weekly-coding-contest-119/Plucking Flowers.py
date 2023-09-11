#User function Template for python3
class Solution:
    # Version 1: Top down DP
    # TC: O(nk), SC: O(nk)
    '''
    def maximumBeauty(self, N, K, B):
        # code here
        
        def pick(index, count, dp):
            if count == K:
                return 0
            if index >= N:
                return float('-inf')
            if (index, count) in dp:
                return dp[index, count]
            res = max(pick(index + 1, count, dp), B[index] + pick(index + 2, count + 1, dp))
            dp[index, count] = res
            return res
        
        dp = {}
        ans = pick(0, 0, dp)
        return ans
    '''
    
    # Version 2: Bottom up DP
    # TC: O(nk), SC: O(nk)
    '''
    def maximumBeauty(self, N, K, B):
        # code here
        dp = [[float('-inf')]*(N + 1) for _ in range(K + 1)]
        dp[0] = [0]*(N + 1)
        for count in range(1, K + 1):
            for i in range(N):
                dp[count][i + 1] = dp[count][i]
                if i > 0:
                    dp[count][i + 1] = max(dp[count][i + 1], dp[count - 1][i - 1] + B[i])
                else:
                    if count == 1:
                        dp[count][i + 1] = max(dp[count][i + 1], B[i])
        return dp[K][N]
    '''    

    # Version 3: Improved version 2
    # TC: O(nk), SC: O(n)
    def maximumBeauty(self, N, K, B):
        # code here
        dp = [0]*(N + 1)
        nextDp = [float('-inf')]*(N + 1)
        for count in range(1, K + 1):
            nextDp[0] = float('-inf')
            for i in range(N):
                nextDp[i + 1] = nextDp[i]
                if i > 0:
                    nextDp[i + 1] = max(nextDp[i + 1], dp[i - 1] + B[i])
                else:
                    if count == 1:
                        nextDp[i + 1] = max(nextDp[i + 1], B[i])
            dp, nextDp = nextDp, dp
        return dp[N]

