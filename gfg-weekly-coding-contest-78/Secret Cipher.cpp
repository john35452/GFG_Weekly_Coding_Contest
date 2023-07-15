//User function Template for C++

// return a string formed by compressing string s
// do not print anything
class Solution{
public:
    // Version 1: Greedy with KMP
    // TC: O(n), SC: O(n)
    string secretCipher(string& s){
        // Code here
        int n = s.size();
        vector<int> pi(2, 0);
        int p = 0;
        for (int i = 1; i < n; i++) {
            while (p > 0 && s[i] != s[p]) {
                p = pi[p];
            }
            if (s[i] == s[p]) p++;
            pi.emplace_back(p);
        }
        
        vector<char> ans;
        int j = n - 1;
        while (j >= 0) {
            if (j % 2 > 0 && check(j, s, pi)) {
                ans.emplace_back('*');
                j /= 2;
            } else {
                ans.emplace_back(s[j]);
                j--;
            }
        }
        
        return string(ans.rbegin(), ans.rend());
    }
    
    bool check(int j, string& s, vector<int>& pi) {
        int leng = pi[j] + 1;
        if (2 * leng < j + 1) return false;
        int half = (j + 1) / 2;
        for (int i = 0; i < half; i++) {
            if (s[i] != s[half + i]) return false;
        }
        return true;
    }
};