class Solution {
public:
  // Version 1: Check cycle size
  // There is no way to reproduce a cycle with size n
  // Therefore, if any node is not included in the cycle, the length of cycle is not n.
  // We can check whether any node's outgoing edge count is 1 
  // which means this node is not included in the cycle.
  // TC: O(V) = O(n), SC: O(n)
  string cyclicTree(int N, vector<vector<int>> &edges) {
    // code here
    vector<vector<int>> graph(N, vector<int>());
    for (int i = 0; i < edges.size(); i++) {
        graph[edges[i][0] - 1].push_back(edges[i][1] - 1);
        graph[edges[i][1] - 1].push_back(edges[i][0] - 1);
    }
    
    for (int i = 0; i < N; i++) {
        if (graph[i].size() == 1) {
            return "Yes";
        }
    }
    return "No";
  }
};