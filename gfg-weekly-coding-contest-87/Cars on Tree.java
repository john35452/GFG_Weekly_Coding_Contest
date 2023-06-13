//User function Template for Java

class Solution
{
    // Version 1: 2 DFS
    // The first DFS to get the nearest distance to a leaf from each node
    // It will be used when a car running out of fuel.
    // The second DFS will get the maximum time needed among the child nodes.
    // TC: O(n), SC: O(n)
    static long solve(int n, int K, int Par[])
    {
        // add your code here
        ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) graph.add(new ArrayList<Integer>());
        
        for (int i = 1; i < n; i++) {
            graph.get(Par[i] - 1).add(i);
        }
        
        int[] leafDis = new int[n];
        long ans = 0;
        dfs(0, graph, leafDis);
        return dfs2(0, K, K, graph, leafDis);
    }
    
    static int dfs(int node, ArrayList<ArrayList<Integer>> graph, int[] leafDis) {
        int res = Integer.MAX_VALUE;
        for (int child: graph.get(node)) {
            res = Math.min(res, dfs(child, graph, leafDis) + 1);
        }
        res = (res == Integer.MAX_VALUE? 0: res);
        leafDis[node] = res;
        return res;
    }
    
    static long dfs2(int node, int fuel, int K, ArrayList<ArrayList<Integer>> graph, int[] leafDis) {
        long res = 0;
        long childCost = 0;
        if (fuel == 0) {
            res += leafDis[node];
            fuel = K;
        }
        for (int child: graph.get(node)) {
            childCost = Math.max(childCost, dfs2(child, fuel - 1, K, graph, leafDis) + 1);
        }
        
        return res + childCost;
    }
}