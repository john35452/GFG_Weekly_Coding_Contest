//User function Template for C++

class Solution {
  public:
    // Version 1: Greedy
    // If there are more than one employees in the same name group within the group, 
    // they won't focus on work.
    // Therefore, we only can make one employee in every name group to focus on work.
    // TC: O(n), SC: O(26) = O(1)
    int splitEmployees(int n, string s[]) {
        // code here
        int fre[26] = {0};
        for (int i = 0; i < n; i++) {
            fre[s[i][0] - 'a']++;
        }
        
        int ans = 0;
        for (int i = 0; i < 26; i++) {
            fre[i]--;
            if (fre[i] > 1) ans += fre[i];
        }
        return ans;
    }
};