from typing import List


class Solution:
    # Version 1: Maximum and Minimum value
    # TC: O(n), SC: O(n)
    def totalCuts(self, N : int, K : int, A : List[int]) -> int:
        # code here
        left = [0]*N
        right = [0]*N
        
        maxv = 0
        minv = float('inf')
        for i in range(N):
            maxv = max(maxv, A[i])
            minv = min(minv, A[N - 1 - i])
            left[i] = maxv
            right[N - 1 - i] = minv
        
        ans = 0
        for i in range(1, N):
            if left[i - 1] + right[i] >= K:
                ans += 1
        return ans