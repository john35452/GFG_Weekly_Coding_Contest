//User function Template for C++

class Solution {
public:

    // Version 1: DFS
    // We can reduce leaf by moving leaf to the child of another leaf.
    // By doing this, we can increase one non-leaf and decease one leaf.
    // Therefore, we can count the leaf count and non-leaf count to count.
    // TC: O(n), SC: O(n)
    /*
    int solve(int N,int Par[]){
        vector<vector<int>> graph(N);
        for (int i = 1; i < N; i++) {
            graph[Par[i] - 1].emplace_back(i);
        }
        
        vector<int> nodes = dfs(0, graph);
        //cout << nodes[0] << " " << nodes[1] << endl;
        if (nodes[1] * 2 < nodes[0]) return 0;
        int non_leaf = nodes[0] - nodes[1];
        int leaf = nodes[1];
        if (leaf == 1) return -1;
        else return ((leaf - non_leaf) / 2) + 1;
    }

    vector<int> dfs(int node, vector<vector<int>>& graph) {
        if (graph[node].size() == 0) {
            return vector<int> {1, 1};
        } 
        vector<int> res {1, 0};
        for (int child: graph[node]) {
            vector<int> tmp = dfs(child, graph);
            res[0] += tmp[0];
            res[1] += tmp[1];
        }
        return res;
    }
    */
    
    // Version 2: Improved version 1
    // TC: O(n), SC: O(n)
    int solve(int N,int Par[]){
        vector<vector<int>> graph(N);
        for (int i = 1; i < N; i++) {
            graph[Par[i] - 1].emplace_back(i);
        }
        
        int leaf = 0;
        for (int i = 1; i < N; i++) {
            if (graph[i].size() == 0) {
                leaf++;
            }
        }
        int non_leaf = N - leaf;
        if (non_leaf > leaf) return 0;
        if (leaf == 1) return -1;
        else return ((leaf - non_leaf) / 2) + 1;
    }
};