class Solution {
  public:
    
    // Version 1: DP
    // dp[i][0 or 1]: The maximum number of flowers can be saved with or without lid be shifted in a[i:]
    // TC: O(n), SC: O(n)
    /*
    int saveFlowers(int n, vector<int> &arr, string s) {
        // code here
        vector<vector<int>> dp(n, vector<int>(2, -1));
        return save(0, 0, s, arr, dp);
    }
    
    int save(int index, int moved, string s, vector<int> &arr, vector<vector<int>>& dp) {
        if (index == s.size()) {
            return 0;
        } else if (dp[index][moved] < 0) {
            int res = 0;
            if (s[index] == '0' || (s[index] == '1' && moved > 0)) {
                res = max(res, save(index + 1, 0, s, arr, dp));
            }
            
            if (s[index] == '1' && moved == 0) {
                res = max(res, arr[index] + save(index + 1, 0, s, arr, dp));
            }
            
            if (index + 1 < s.size() && s[index + 1] == '1') {
                if (s[index] == '0' || (s[index] == '1' && moved > 0)) {
                    res = max(res, arr[index] + save(index + 1, 1, s, arr, dp));
                }
            }
            dp[index][moved] = res;
        }
        return dp[index][moved];
    }
    */
    
    
    // Version 2: Greedy
    // We can start in revered direction because the lid only can be shifted to left hand side.
    // When we meet lid, we can include one more number before consecutive 1, and drop the minimum value among them.
    // Because we can shift all lids staring from that number to the left hand side.
    // For the ending part, since we cannot shift, we can need to add sum to the final result.
    // TC: O(n), SC: O(1)
    int saveFlowers(int n, vector<int> &arr, string s) {
        // code here
        int ans = 0;
        int minv = INT_MAX;
        bool hasLid = false;
        int sum = 0;
        for (int i = n - 1; i >= 0; i--) {
            if (s[i] == '1') {
                hasLid = true;
                minv = min(minv, arr[i]);
                sum += arr[i];
            } else {
                if (hasLid) {
                    minv = min(minv, arr[i]);
                    sum += arr[i];
                    hasLid = false;
                    ans += sum - minv;
                    sum = 0;
                    minv = INT_MAX;
                }
            }
        }
        if (hasLid) {
            ans += sum;
        }
        return ans;
    }
};