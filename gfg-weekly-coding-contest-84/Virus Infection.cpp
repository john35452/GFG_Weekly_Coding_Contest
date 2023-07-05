//User function Template for C++

class Solution{
    public:
    // Version 1: DP
    // Memory the diff and get the number of overlapping virus at each moment
    // TC: O(n), SC: O(n)
    /*
    int solve(string s, int K){
        // code here
        int n = s.size();
        int diff[n + 1] = {0};
        for (int i = 0; i < n; i++) {
            if (s[i] == '1') {
                diff[max(i - K, 0)]++;
                diff[min(i + K + 1, n)]--;
            }
        }
        int ans = 0;
        int current = 0;
        for (int i = 0; i < n; i++) {
            current += diff[i];
            if (current > 0)ans++;
        }
        return ans;
    }
    */
    
    // Version 2: BFS
    // TC: O(n), SC: O(n)
    int solve(string s, int K){
        // code here
        int n = s.size();
        deque<int> q;
        vector<bool> used(n, false);  
        for (int i = 0; i < n; i++) {
            if (s[i] == '1') {
                q.emplace_back(i);
                used[i] = true;
            }
        }
              
        for (int i = 0; i < K; i++) {
            int size = q.size();
            for (int j = 0; j < size; j++) {
                int index = q.front();
                q.pop_front();
                if (index - 1 >= 0 && (!used[index - 1])) {
                    used[index - 1] = true;
                    q.emplace_back(index - 1);
                }
                
                if (index + 1 < n && (!used[index + 1])) {
                    used[index + 1] = true;
                    q.emplace_back(index + 1);
                }
            }
        }
        
        int ans = 0;
        for (int i = 0; i < n; i++) {
            if (used[i])ans++;
        }
        return ans;
    }
};