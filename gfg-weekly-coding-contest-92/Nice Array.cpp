class Solution {
  public:
    // Version 1: Count consecutive numbers
    // TC: O(n), SC: O(1)
    int niceSubarray(int n, vector<int> &arr) {
        // code here
        int num = 1;
        int ans = 0;
        for (int val: arr) {
            if (val == num) {
                num += 1;
                ans = max(ans, num - 1);
            } else {
                if (val == 1) {
                    num = 2;
                } else {
                    num = 1;
                }
            }
        }
        ans = max(ans, num - 1);
        return ans;
    }
};