// User function Template for C++

class Solution {
  public:
    // Version 1: Stack
    // TC: O(n), SC: O(n)
    int finLength(int N, vector<int> color, vector<int> radius) {
        // code here
        stack<int> st;
        for (int i = 0; i < N; i++) {
            if (!st.empty() && color[st.top()] == color[i] && radius[st.top()] == radius[i]) {
                st.pop();
            } else {
                st.emplace(i);
            }
        }
        return st.size();
    }
};