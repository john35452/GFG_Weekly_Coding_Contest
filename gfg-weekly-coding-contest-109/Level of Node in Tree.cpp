
class Solution {
  public:
    // Version 1: Count
    // TC: O(logn) = O(1), SC: O(1)
    long long findLevel(long long N) {
        // code here
        long long cur = 1;
        long long level = 1;
        long long count = 0;
        while (count < N) {
            count += cur;
            cur *= (level + 1);
            level++;
        }
        return level - 1;
    }
};