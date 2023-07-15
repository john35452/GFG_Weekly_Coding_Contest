
class Solution {
  public:
    // Version 1: Greedy
    // We can make any subarray without zero to all zero with one operation.
    // Therefore, we can count the number of longest non-zero subarrays.
    // However, we always can do one things.
    // Choose the whole array, and set them all to MEX
    // Then choose the whole array again to set them to 0.
    // Therefore, we can always make it to 0 with at most 2 operations.
    // TC: O(n), SC: O(1)
    int arrayOperations(int n, vector<int> &arr) {
        // code here
        int non_zero = 0, l = 0;
        for (int i = 0; i < n; i++) {
            if (arr[i] == 0) {
                if (i > l) non_zero++;
                l = i + 1;
            }
        }
        if (l < n) non_zero++;
        if (non_zero < 2) return non_zero;
        else return 2;
    }
};