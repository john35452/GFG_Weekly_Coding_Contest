//User function Template for C++

class Solution {
  public:
    // Version 1: Bit mask
    // Try all possibility on columns, and get the most beneficial count from each row.
    // TC: O(2^m * n), SC: O(mn)
    int optimalMoves(int n,int m, vector<vector<int>>grid) {
        // code here
        int ans = 0;
        vector<vector<int>> newGrid(n, vector<int>(m, 0));
        for (int mask = 0; mask < (1<<m); mask++) {
            for (int i = 0; i < m; i++) {
                int flip = ((mask & (1<<i)) > 0 ? 1 : 0);
                for (int j = 0; j < n; j++) {
                    newGrid[j][i] = grid[j][i] ^ flip;
                }
            }
            
            int res = 0;
            for (int i = 0; i < n; i++) {
                int one = 0;
                for (int j = 0; j < m; j++) 
                    if (newGrid[i][j] > 0) one++;
                res += max(one, m - one);
            }
            ans = max(ans, res);
        }
        return ans;
    }
};