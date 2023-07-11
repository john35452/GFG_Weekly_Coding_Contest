class Solution {
  public:
    // Version 1: Memorize the next available time for each element
    // TC: O(n), SC: O(n)
    int totalTime(int n, vector<int> &arr, vector<int> &time) {
        // code here
        int t = 0;
        vector<int> valid(n + 1, 0);
        for (int i = 0; i < n; i++) {
            t = max(t, valid[arr[i]]);
            valid[arr[i]] = t + time[arr[i] - 1];
            t++;
        }
        return t - 1;
    }
};