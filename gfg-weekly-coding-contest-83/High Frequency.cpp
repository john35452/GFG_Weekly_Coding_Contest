//User function Template for C++

class Solution {
  public:
    // Version 1: Most frequent alphbet
    // If the most frequent subarray is not a alphbet.
    // The frequency of all alphbets in the subarray most be at least the same as the subarray.
    // Therefore, we can just find the most frequent alphbet
    // TC: O(n), SC: O(1)
    string solve(int N, string S) {
        // code here
        vector<int> fre(26, 0);
        for (int i = 0; i < N; i++) {
            fre[S[i] - 'a']++;
        }
        
        auto max = max_element(fre.begin(), fre.end());
        return string {(char)('a' + max - fre.begin())};
    }
};