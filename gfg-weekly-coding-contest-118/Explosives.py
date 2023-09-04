#User function Template for python3
from typing import List

class Solution:
    # Version 1: Preprocess and DP
    # TC: O(n^2), SC: O(n^2)
    '''
    def maxBoxes(self, N : int, K : int , C : int, col : List[int]):
        # code here 
        
        def explode(i, j, dp):
            if (i, j) in dp:
                return dp[i, j]
            left_col = right_col = None
            left_count = right_count = 0
            res = 0
            if i >= 0:
                left_col, left_count = box[i]
            if j < m:
                right_col, right_count = box[j]
            if left_col == right_col and left_count + right_count >= 3:
                res = left_count + right_count + explode(i - 1, j + 1, dp)
            dp[i, j] = res
            return dp[i, j]
            
            
        dp = {}
        box = []
        pre = None
        count = 0
        for i in range(N):
            if col[i] == pre:
                count += 1
            else:
                if count > 0:
                    box.append([pre, count])
                pre = col[i]
                count = 1
        if count > 0:
            box.append([pre, count])
        m = len(box)
        ans = 0
        for i in range(m):
            if box[i][0] == C:
                if box[i][1] >= 2:
                    ans = max(ans, box[i][1] + explode(i - 1, i + 1, dp))
        return ans
    '''
    
    # Version 2: Remove DP
    # TC: O(n^2), SC: O(1)
    def maxBoxes(self, N : int, K : int , C : int, col : List[int]):
        # code here 
        ans = 0
        for i in range(N):
            if col[i] == C:
                l = r = i
                start = 1
                total = 0
                count = 1
                while l >= 0 and r < N and col[l] == col[r]:
                    target = col[l]
                    while l > 0 and col[l - 1] == target:
                        l -= 1
                        count += 1
                    while r + 1 < N and col[r + 1] == target:
                        r += 1
                        count += 1
                    if count >= 3 - start:
                        total += count 
                    else:
                        break
                    start = 0
                    count = 2
                    l -= 1
                    r += 1
                ans = max(ans, total)
        return ans

