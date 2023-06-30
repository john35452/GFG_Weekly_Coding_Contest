//User function Template for C++
class Solution
{
    public:
    // Version 1: Cut from every edge in DFS
    // TC: O(n), SC: O(n)
    long long MinDiff(int n, int A[], int B[])
    {
        //Write Code Here
        vector<vector<int>> graph(n + 1, vector<int>());
        for (int i = 0; i < n - 1; i++) {
            graph[A[i]].emplace_back(B[i]);
            graph[B[i]].emplace_back(A[i]);
        }
        long long total = 1LL * n * (n + 1) / 2;
        long long ans = LLONG_MAX;
        for (int child: graph[1]) {
            dfs(child, 1, graph, total, &ans);
        }
        return ans;
    }
    
    long long dfs(int node, int parent, vector<vector<int>>& graph, long long total, long long* ans) {
        long long res = node;
        for (int child: graph[node]) {
            if (child != parent) {
                res += dfs(child, node, graph, total, ans);
            }
        }
        *ans = min(*ans, abs(total - 2 * res));
        return res;
    }
};