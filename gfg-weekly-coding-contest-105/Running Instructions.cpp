
class Solution {
  public:
    // Version 1: BFS
    // TC: O(nm), SC: O(m)
    /*
    string instructionCheck(int m, int n, vector<int> &k) {
        // Code Here.
        unordered_set<int> current, nextStep;
        current.insert(k[0]);
        int val;
        for (int i = 1; i < n; i++) {
            while (!current.empty()) {
                val = *current.begin();
                current.erase(current.begin());
                nextStep.insert((val + k[i] % m + m) % m);
                nextStep.insert((val - k[i] % m + m) % m);
            }
            unordered_set<int> tmp = current;
            current = nextStep;
            nextStep = tmp;
        }
        
        if(current.find(0) != current.end()) {
            return "YES";
        } else {
            return "NO";
        }
    }
    */
    
    // Version 2: DP
    // TC: O(mn), SC: O(mn)
    string instructionCheck(int m, int n, vector<int> &k) {
        // Code Here.
        vector<vector<int>> dp(n, vector<int>(m + 1, -1));
        if (run(0, 0, m, k, dp) > 0) {
            return "YES";
        } else {
            return "NO";
        }
    }
    
    int run(int index, int score, int m, vector<int> &k, vector<vector<int>>& dp) {
        if (index == k.size()) {
            if (score == 0) return 1;
            else return 0;
        } else if (dp[index][score] == -1) {
            dp[index][score] = max(
                run(index + 1, (score + k[index] % m + m) % m, m, k, dp), 
                run(index + 1, (score - k[index] % m + m) % m, m, k, dp)
            );
        }
        return dp[index][score];
    }
};