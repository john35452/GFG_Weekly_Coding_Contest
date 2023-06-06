from typing import List

class Solution:
    # Version 1: DP and rule
    # For each diffence between the role, the path sum will be 2k.
    # If there is a path with path sum smaller than the maximum path sum, there must be a path with only one cell difference and 2k value difference.
    # Path sum 4:
    # 2(v)  -2(v)  -2    -2
    # -2     2(v)  2(v)  -2
    # 2      2     2(v)  -2(v)
    
    # We can change to path sum 0 by only changing one cell.
    # 2(v)  -2(v)  -2    -2
    # -2     2(v)  2(v)  -2(v)
    # 2      2     2     -2(v)
    
    # Therefore, we can get the maximum and minimum path sum, and get the result by checking val % 2k
    # TC: O(mn + q), SC; O(mn)
    def possiblePathSum(self, n : int, m : int, grid : List[List[int]], q : int, queries : List[int]) -> List[int]:
        # Code Here
        maxv = [[0 for _ in range(m)] for i in range(n)]
        minv = [[0 for _ in range(m)] for i in range(n)]
        
        maxv[0][0] = minv[0][0] = grid[0][0]
        
        for i in range(1, n):
            maxv[i][0] = maxv[i - 1][0] + grid[i][0]
            minv[i][0] = minv[i - 1][0] + grid[i][0]
        
        for i in range(1, m):
            maxv[0][i] = maxv[0][i - 1] + grid[0][i]
            minv[0][i] = minv[0][i - 1] + grid[0][i]
            
        for i in range(1, n):
            for j in range(1, m):
                maxv[i][j] = max(maxv[i][j - 1], maxv[i - 1][j]) + grid[i][j]
                minv[i][j] = min(minv[i][j - 1], minv[i - 1][j]) + grid[i][j]
        
        k = abs(grid[0][0])
        ans = []
        for val in queries:
            if (val < minv[-1][-1] or val > maxv[-1][-1]):
                ans.append(0)
            elif ((val - minv[-1][-1]) % (2 * k) == 0):
                ans.append(1)
            else:
                ans.append(0)
        return ans
            