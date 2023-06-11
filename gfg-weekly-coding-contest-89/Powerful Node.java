

//User function Template for Java

class Solution{
    
    // Version 1: Reroot(2 DFS)
    // Consider one node as the root and use dfs calculate Power(root)
    // We can store the sum of all nodes' id under each node which can be used to recalculate Power(i).
    // For the reroot, we can apply another dfs and calculate other nodes' power base on the power of last root.
    // Let say we move from root i to j and the original root is 0.
    // When we move from root i to j, all distance between nodes under j decrease 1, and all other nodes increase 1.
    // The value change for nodes under node j, is the sum of ids among those nodes which is nodeWeight[j].
    // For other nodes change is also the sum of ids which is nodeWeight[0] - nodeWeight[j].
    // As the result, we know the below transformation.
    // Power(j) = Power(i) + 1 * (nodeWeight[0] - nodeWeight[j]) - 1 * (nodeWeight[j])
    //          = Power(i) + nodeWeight[0] - 2 * nodeWeight[j]
    // TC: O(n), SC: O(n)
    static int maxPower(int n, int edges[][]){
        // Code Here. 
        ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) graph.add(new ArrayList<Integer>());
        
        for (int[] edge: edges) {
            graph.get(edge[0]).add(edge[1]);
            graph.get(edge[1]).add(edge[0]);
        }
        
        long nodeWeight[] = new long[n];
        long power[] = new long[n];
        long[] p = dfs(0, -1, 0, graph, nodeWeight);
        dfs2(0, -1, p[0], graph, power, nodeWeight);
        int ans = 0;
        for (int i = 0; i < n; i++) {
            if (power[ans] < power[i]) ans = i;
        }
        return ans;
    }
    
    static long[] dfs(int node, int par, int depth, ArrayList<ArrayList<Integer>> graph, long nodeWeight[]) {
        long p = node * depth;
        long weight = 1L * node;
        for (int child : graph.get(node)) {
            if (child != par) {
                long[] res = dfs(child, node, depth + 1, graph, nodeWeight);
                p += res[0];
                weight += res[1];                
            }
        }
        nodeWeight[node] = weight;
        return new long[] {p, weight};
    }
    
    static void dfs2(int node, int parent, long newPower, ArrayList<ArrayList<Integer>> graph, long[] power, long[] nodeWeight) {
        power[node] = newPower;
        for (int child : graph.get(node)) {
            if (child != parent) {
                dfs2(child, node, newPower + nodeWeight[0] - 2 * nodeWeight[child], graph, power, nodeWeight);
            }
        }
    }
    
}