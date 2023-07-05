//User function Template for C++
class Fenwick {
    public:
        vector<int> data;
        Fenwick(int n) {
            data = vector<int>(n + 1, 0);
        }
        
        void update(int index, int delta) {
            index++;
            while (index < data.size()) {
                data[index] += delta;
                index += (index & -index);
            }
        }
        
        int prefix(int index) {
            int ans = 0;
            index++;
            while (index > 0) {
                ans += data[index];
                index -= (index & -index);
            }
            return ans;
        }
};

class Solution{
    public:
    // Version 1: Post order traversal
    // Get the valid sequence of the nodes
    // TC: O(n^2), SC: O(n)
    /*
    vector<int> labelTree(int N, vector<int> p){
        // code here
        vector<vector<int>> graph(N);
        for (int i = 1; i < N; i++) {
            graph[p[i]].emplace_back(i);
        }
        
        vector<int> order = postorder(0, graph);
        vector<int> res(N);
        for (int i = 0; i < N; i++) {
            res[order[i]] = i + 1;
        }
        
        return res;
    }
    
    vector<int> postorder(int node, vector<vector<int>>& graph) {
        if (graph[node].size() == 0) {
            return vector<int> {node};
        } else {
            vector<int> res;
            for (int child: graph[node]) {
                vector<int> tmp = postorder(child, graph);
                res.insert(res.end(), tmp.begin(), tmp.end());
            }
            res.insert(res.begin() + (res.size()) / 2, node);
            return res;
        }
    }
    */
    
    // Version 2: Fill in the value from root
    // Choose from the non-chosen values
    // Use Fenwick tree to record the unused numbers
    // TC: O(nloglogn), SC: O(n)
    vector<int> labelTree(int N, vector<int> p){
        // code here
        vector<vector<int>> graph(N);
        for (int i = 1; i < N; i++) {
            graph[p[i]].emplace_back(i);
        }
        
        Fenwick bit(N);
        for (int i = 0; i < N; i++) {
            bit.update(i, 1);
        }
        
        vector<int> treeSize(N);
        dfs(0, graph, treeSize);
        vector<int> res(N);
        dfs2(0, N, graph, treeSize, bit, res);
        return res;
    }
    
    void dfs2(int node, int N, vector<vector<int>>& graph, vector<int>& treeSize, Fenwick& bit, vector<int>& ans) {
        int pre = 1 + (treeSize[node] - 1) / 2;
        int l = 0, r = N - 1;
        while (l < r) {
            int m = l + (r - l) / 2;
            if (bit.prefix(m) >= pre) {
                r = m;
            } else {
                l = m + 1;
            }
        }
        ans[node] = l + 1;
        bit.update(l, -1);
        for (int child: graph[node]) {
            dfs2(child, N, graph, treeSize, bit, ans);
        }
    }
    
    int dfs(int node, vector<vector<int>>& graph, vector<int>& tree) {
        int res = 1;
        for (int child: graph[node]) {
            res += dfs(child, graph, tree);
        }
        tree[node] = res;
    }
};