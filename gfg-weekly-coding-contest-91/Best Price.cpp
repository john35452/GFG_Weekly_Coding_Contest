//User function Template for C++


class Solution {
  public:
    
    // Version 1: Prefix sum
    // Store difference for each price range, and go through them once to know overlapping count for each time
    // Check whether the time is valid, and calculate the presum sum of the result.
    // TC: O(n + q + max(price, queries)), SC: O(max(price, queries))
    vector<int> bestPrice(int n,vector<vector<int>> price,int k,int q, vector<vector<int>> queries) {
        // code here
        int maxv = INT_MIN;
        for (int i = 0; i < n; i++) maxv = max(maxv, price[i][1]);
        for (int i = 0; i < q; i++) maxv = max(maxv, queries[i][1]);
        
        vector<int> diff(maxv + 2);
        for (int i = 0; i < n; i++) {
            diff[price[i][0]] += 1;
            diff[price[i][1] + 1] -= 1;
        }
        
        vector<int> prefix(maxv + 2);
        int current = 0;
        for (int i = 0; i <= maxv; i++) {
            current += diff[i];
            prefix[i + 1] = prefix[i] + (current >= k ? 1: 0);
        }
        
        vector<int> ans(q);
        for (int i = 0; i < q; i++) {
            ans[i] = prefix[queries[i][1] + 1] - prefix[queries[i][0]];
        }    
        return ans;
    }
};