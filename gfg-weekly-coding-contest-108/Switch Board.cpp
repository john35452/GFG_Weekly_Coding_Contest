//User function Template for C++
class Solution
{
    public:
    // Version 1: Top down DP
    // TC: O(mn), SC: O(n)
    /*
    long long MinCost(string s, int m, int costs[])
    {
        //Write Code Here
        int n = s.size();
        vector<long long>dp(n + 1, LLONG_MAX);
        return turn(0, s, costs, m, dp);
    }
    
    long long turn(int index, string s, int costs[], int m, vector<long long>& dp) {
        if (index >= s.size()) return 0;
        else if (dp[index] != LLONG_MAX) return dp[index];
        
        long long res = LLONG_MAX;
        if (s[index] == '1') res = min(res, turn(index + 1, s, costs, m, dp));
        else {
            for (int i = 0; i < m; i++) {
                res = min(res, costs[i] + turn(index + i + 1, s, costs, m, dp)); 
            }
        }
        dp[index] = res;
        return dp[index];
    }
    */
    
    // Version 2: Bottom up DP
    // TC: O(mn), SC: O(n)
    long long MinCost(string s, int m, int costs[])
    {
        //Write Code Here
        int n = s.size();
        vector<long long>dp(n + 1, pow(10, 14));
        dp[0] = 0;
        for (int i = 0; i < n; i++) {
            if (s[i] == '1') dp[i + 1] = dp[i];
            else {
                for (int j = 0; j < m; j++) {
                    dp[i + 1] = min(dp[i + 1], (long long)costs[j] + dp[max(i - j, 0)]);
                }    
            }
        }
        return dp[n];
    }
};