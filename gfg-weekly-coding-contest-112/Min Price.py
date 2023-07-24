from typing import List


class Solution:
    # Version 1: Top down DP
    # We need to check whether free count is more than the remaining items.
    # Otherwise, we might 500 * 500 * 500 which is O(n^3) space for the dp.
    # TC: O(n^2), SC: O(n * 2n)
    def minCost(self, n : int, p : List[int], f : List[int]) -> int:
        # code here
        
        def buy(index, free, dp):
            if index == n:
                if free >= 0:
                    return 0
                else:
                    return float('inf')
            if free >= n - index:
                return 0
            if (index, free) in dp:
                return dp[index, free]
            res = min(p[index] + buy(index + 1, free + f[index], dp), 
                      buy(index + 1, free - 1, dp))
            dp[index, free] = res
            return dp[index, free]
        
        dp = {}
        ans = buy(0, 0, dp)
        return ans
            