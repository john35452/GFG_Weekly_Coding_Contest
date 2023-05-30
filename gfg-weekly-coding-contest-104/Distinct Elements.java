

//User function Template for Java
class Solution 
{ 
    // Version 1: BFS
    // TC: O(N), SC: (N)
    /*
    double density(int N, int par[]) 
    { 
        // code here
        int root = -1;
        Map<Integer, ArrayList<Integer>> graph = new HashMap<>();
        for (int i = 0; i < N; i++) {
            graph.put(i, new ArrayList<Integer>());
        }
        for (int i = 0; i < N; i++) {
            if (par[i] == -1) {
                root = i;
            } else {
                graph.get(par[i]).add(i);
            }
        }
        
        int height = 0;
        Queue<Integer> queue = new LinkedList<Integer>();
        queue.offer(root);
        
        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                int node = queue.poll();
                for (int child : graph.get(node)) {
                    queue.offer(child);
                }
            }
            height += 1;
        }
        
        return 1.0 * N / height;
    }
    */
    
    // Version 2: DFS
    // TC: O(n), SC: O(n)
    double density(int N, int par[]) 
    { 
        // code here
        int root = -1;
        ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            graph.add(new ArrayList<Integer>());
        }
        for (int i = 0; i < N; i++) {
            if (par[i] == -1) {
                root = i;
            } else {
                graph.get(par[i]).add(i);
            }
        }
        
        int height = dfs(root, graph);
        return 1.0 * N / height;
    }
    
    private int dfs(int node, ArrayList<ArrayList<Integer>> graph) {
        int res = 0;
        for (int child: graph.get(node)) {
            res = Math.max(res, dfs(child, graph));
        }
        return res + 1;
        
    }
} 