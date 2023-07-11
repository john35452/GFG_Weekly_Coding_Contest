
class Solution {
  public:
    // Version 1: Count
    // TC: O(n), SC: O(1)
    int separateStones(int N, int K, vector<int> &arr) {
        // code here
        int fre[2] = {0, 0};
        for (int val: arr) {
            fre[val]++;
        }
        int ans = 0;
        for (int val: fre) {
            ans += ceil(1.0*val / K);
        }
        return ans;
    }
};