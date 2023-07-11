class Solution {
  public:
    // Version 1: Stack
    // Consider the positive and negative diff respectively
    // TC: O(n), SC: O(n)
    /*
    long long minimumMoves(int n, vector<int> &a, vector<int> &b) {
        // code here
        vector<int> diff_a(n, 0), diff_b(n, 0);
        for (int i = 0; i < n; i++) {
            if (a[i] > b[i]) {
                diff_a[i] = a[i] - b[i];
            } else {
                diff_b[i] = b[i] - a[i];
            }
        }
        
        return getCount(diff_a) + getCount(diff_b);
    }
    
    long long getCount(vector<int>& diff) {
        long long ans = 0;
        stack<int> st;
        diff.emplace_back(0);
        for (int val: diff) {
            while (!st.empty() && val <= st.top()) {
                int t = st.top();
                st.pop();
                int left = val;
                if (!st.empty()) left = max(left, st.top());
                ans += t - left;
            }
            st.push(val);
        }
        return ans;
    }
    */
    
    // Version 2: Improved version 1
    // Increase answer when we meet a new diff bigger than previous diff
    // TC: O(n), SC: O(1)
    long long minimumMoves(int n, vector<int> &a, vector<int> &b) {
        // code here
        int preP = 0, preN = 0;
        long long ans = 0;
        for (int i = 0; i < n; i++) {
            int diff = a[i] - b[i];
            if (diff >= 0) {
                if (diff > preP) {
                    ans += diff - preP;
                }
                preP = diff;
                preN = 0;
            } else {
                diff *= -1;
                if (diff > preN) {
                    ans += diff - preN;
                }
                preN = diff;
                preP = 0;
            }
        }
        return ans;
    }
};