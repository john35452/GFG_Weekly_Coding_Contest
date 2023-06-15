

//User function Template for Java

class Solution{
    
    // Version 1: DFS
    // Create from root and count
    // It will overflow due to the recursion stack size
    // TC: O(n), SC: O(n)
    /*
    static long minimumCost(int n, int p[]){
        ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) graph.add(new ArrayList<Integer>());
        int root = 0;
        for (int i = 0; i < n; i++) {
            if (p[i] > 0) {
                graph.get(p[i] - 1).add(i);
            } else {
                root = i;
            }
        }
        
        return dfs(root, 0L, graph);
    }
    
    static long dfs(int node, long degree, ArrayList<ArrayList<Integer>> graph) {
        long res = 0;
        for (int child: graph.get(node)) {
            degree++;
            res += degree + dfs(child, 1L, graph);
        }
        return res;
    } 
    */
    
    // Version 2: BFS version of version 1
    // TC: O(n), SC: O(n)
    /*
    static long minimumCost(int n, int p[]){
        ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) graph.add(new ArrayList<Integer>());
        int root = 0;
        for (int i = 0; i < n; i++) {
            if (p[i] > 0) {
                graph.get(p[i] - 1).add(i);
            } else {
                root = i;
            }
        }
        long ans = 0;
        Deque<int[]> deque = new ArrayDeque<int[]>();
        deque.offerLast(new int[] {root, 0});
        while (!deque.isEmpty()) {
            int size = deque.size();
            for (int i = 0; i < size; i++) {
                int[] item = deque.pollFirst();
                int degree = item[1];
                for (int child: graph.get(item[0])) {
                    degree++;
                    ans += degree;
                    deque.offerLast(new int[] {child, 1});
                }
            }
        }
        return ans;
    }
    */
    
    // Version 3: Count the indegree and add edge 1 by 1
    // TC: O(n), SC: O(n)
    static long minimumCost(int n, int p[]){
        long ans = 0;
        long indegree[] = new long[n];
        for (int i = 0; i < n; i++) {
            if (p[i] > 0) {
                indegree[p[i] - 1]++;
                indegree[i]++;
                ans += indegree[p[i] - 1] * indegree[i];
            }
        }
        return ans;
    }
    
}