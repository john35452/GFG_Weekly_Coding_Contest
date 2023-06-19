
class Solution {
  public:
    // Version 1: Bitmask DP
    // dp[mask] : The minimum number of positions needs to put students with bitmask mask
    // TC: O(n * 2^n), SC: O(2^n)
    int roomsRequired(int N, int K, vector<int> &students) {
        // code here
        vector<long long> dp(1<<N, LLONG_MAX);
        dp[0] = 0;
        for (int mask = 0; mask < (1<<N); mask++) {
            for (int i = 0; i < N; i++) {
                if ((mask & (1<<i)) == 0) {
                    int room = dp[mask] / K;
                    int count = dp[mask] % K;
                    if (count + students[i] <= K) {
                        count += students[i];
                    } else {
                        room++;
                        count = students[i];
                    }
                    dp[mask | (1<<i)] = min(dp[mask | (1<<i)], 1LL * room * K + count);
                }
            }
        }
        
        int room = dp[(1<<N) - 1] / K;
        int count = dp[(1<<N) - 1] % K;
        return count > 0 ? room + 1: room;
    }
};