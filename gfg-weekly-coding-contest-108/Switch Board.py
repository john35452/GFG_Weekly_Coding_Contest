
from typing import List


class Solution:
    # Version 1: Top down DP
    # TC: O(mn), SC: O(n)
    '''
    def MinCost(self, s : str, m : int, costs : List[int]) -> int:
        # code here
        import sys
        sys.setrecursionlimit(1000000)
        
        def flip(index, dp):
            if index >= n:
                return 0
            elif index in dp:
                return dp[index]
            res = float('inf')
            if s[index] == '1':
                res = flip(index + 1, dp)
            else:
                for i in range(m):
                    res = min(res, costs[i] + flip(index + i + 1, dp))
            dp[index] = res
            return dp[index]
        
        n = len(s)
        dp = {}
        ans = flip(0, dp)
        return ans
    '''
    
    # Version 2: Bottom up DP
    # TC: O(mn), SC: O(n)
    def MinCost(self, s : str, m : int, costs : List[int]) -> int:
        # code here
        n = len(s)    
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(n):
            if s[i] == '1':
                dp[i + 1] = dp[i]
            else:
                for j in range(m):
                    dp[i + 1] = min(dp[i + 1], costs[j] + dp[max(i - j, 0)])
        return dp[-1]
