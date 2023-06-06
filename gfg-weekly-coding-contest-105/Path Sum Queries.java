

class Solution{
    // Version 1: DP and rule
    // For each diffence between the role, the path sum will be 2k.
    // If there is a path with path sum smaller than the maximum path sum, there must be a path with only one cell difference and 2k value difference.
    // Path sum 4:
    // 2(v)  -2(v)  -2    -2
    // -2     2(v)  2(v)  -2
    // 2      2     2(v)  -2(v)
    
    // We can change to path sum 0 by only changing one cell.
    // 2(v)  -2(v)  -2    -2
    // -2     2(v)  2(v)  -2(v)
    // 2      2     2     -2(v)
    
    // Therefore, we can get the maximum and minimum path sum, and get the result by checking val % 2k
    // TC: O(mn + q), SC; O(mn)
    public int[] possiblePathSum(int n, int m, int grid[][], int q, int queries[]){
        // Code Here.
        
        int maxv[][] = new int[n][m];
        int minv[][] = new int[n][m];
        
        maxv[0][0] = minv[0][0] = grid[0][0];
        
        for (int i = 1; i < n; i++) {
            maxv[i][0] = maxv[i - 1][0] + grid[i][0];
            minv[i][0] = minv[i - 1][0] + grid[i][0];
        }
            
        for (int i = 1; i < m; i++) {
            maxv[0][i] = maxv[0][i - 1] + grid[0][i];
            minv[0][i] = minv[0][i - 1] + grid[0][i];
        }
            
        for (int i = 1; i < n; i++) {
            for (int j = 1; j < m; j++) {
                maxv[i][j] = Math.max(maxv[i][j - 1], maxv[i - 1][j]) + grid[i][j];
                minv[i][j] = Math.min(minv[i][j - 1], minv[i - 1][j]) + grid[i][j];
            }
        }
                
        int k = Math.abs(grid[0][0]);
        int ans[] = new int[q];
        for (int i = 0; i < q; i++) {
            int val = queries[i];
            if (val < minv[n - 1][m - 1] || val > maxv[n - 1][m - 1]) {
                ans[i] = 0;
            } else if ((val - minv[n - 1][m - 1]) % (2 * k) == 0) {
                ans[i] = 1;
            } else {
                ans[i] = 0;
            }
        }
        return ans;
    }   
}