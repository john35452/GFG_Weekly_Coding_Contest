#User function Template for python3

class Solution:
    # Version 1: Subset sum DP
    # TC: O(n * X), SC: O(100 * X)
    '''
    def maxRemoval(self, N, A, X):
        #code here
        from collections import Counter
        
        def pick(index, left, used, dp):
            if left == 0:
                return True
            if index == len(fre):
                return False
            if (index, left) in dp:
                return dp[index, left]
            res = False
            for t in range(fre[index][1] + 1):
                if fre[index][0] * t <= left:
                    tmp = pick(index + 1, left - fre[index][0] * t, used, dp)
                    if tmp and t > 0:
                        used.add(fre[index][0])
                    res = res or tmp
                else:
                    break
            dp[index, left] = res
            return res
        
        f = Counter(A)
        fre = sorted(f.items())
        
        dp = {}
        used = set()
        res = pick(0, X, used, dp)
        #print(pick(0, X, used, dp))
        #print(used)
        ans = N
        for k in used:
            ans -= f[k]
        return ans
    '''
    
    # Version 2: Count the number of ways to reach a certain amount
    # dp[val]: The number of ways to reach sum val
    # TC: O(NX), SC: O(N)
    def maxRemoval(self, N, A, X):
        #code here
        M = 10**9 + 7
        dp = [0]*(100 * (N + 1))
        dp[0] = 1
        maxv = 0
        for i in range(N):
            if A[i] > X:
                continue
            for t in range(maxv, -1, -1):
                dp[t + A[i]] = (dp[t + A[i]] + dp[t]) % M
                maxv = max(maxv, t + A[i])
        ans = 0
        for i in range(N):
            if A[i] > X:
                ans += 1
            else:
                for j in range(A[i], X + 1):
                    dp[j] = (dp[j] - dp[j - A[i]]) % M
                if dp[X - A[i]] == 0:
                    ans += 1
                for j in range(X, A[i] - 1, -1):
                    dp[j] = (dp[j] + dp[j - A[i]]) % M
        return ans
        