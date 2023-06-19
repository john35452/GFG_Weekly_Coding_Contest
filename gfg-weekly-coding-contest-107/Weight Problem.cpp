
class Solution {
  public:
    // Version 1: Count 1 in binary representation
    // TC: O(logn), SC: O(logn)
    int nBlocks(int w) {
        // code here
        int ans = 0;
        while (w > 0) {
            ans += (w & 1);
            w >>= 1;
        }
        return ans;
    }
};