

//User function Template for Java

class Solution{
    
    // Version 1: DP
    // Consider the number of consecutive count of a and b until a node
    // dp[i][j][k]: The maximum path sum starting from node i with j chances of a and k chances of b.
    // For dp[i][j][l], whenever j != k, l must be k. Vice versa.
    // So there are at most n * k * 2 state.
    // TC: O(nk), SC: O(nk^2)
    /*
    static long maximumSum(int n, int k, int p[], int a[], int b[]){
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
        
        Long[][][] dp = new Long[n][k + 1][k + 1];
        long ans = dfs(0, k, k, k, graph, a, b, dp);
        return ans;
    }
    
    static long dfs(int node, int cont_p, int cont_n, int k, ArrayList<ArrayList<Integer>> graph, int a[], int b[], Long[][][] dp) {
        if (dp[node][cont_p][cont_n] != null) {
            return dp[node][cont_p][cont_n];
        }
        long ans = Long.MIN_VALUE;
        if (graph.get(node).size() == 0) {
            if (cont_p > 0) ans = a[node];
            else ans = b[node];
        } else {
            for (int child: graph.get(node)) {
                if (cont_p > 0) {
                    ans = Math.max(ans, a[node] + dfs(child, cont_p - 1, k, k, graph, a, b, dp));    
                }
                if (cont_n > 0) {
                    ans = Math.max(ans, b[node] + dfs(child, k, cont_n - 1, k, graph, a, b, dp));    
                }
            }    
        }
        
        dp[node][cont_p][cont_n] = ans;
        return dp[node][cont_p][cont_n];
    }
    */
    
    // Version 2: Another DP
    // dp[i][0 | 1][k]: The maximum path sum until node i with continuous k - 1 0 or 1
    // Since we will add minus number, we cannot initialize dp array to Long.MIN_VALUE.
    // Otherwise, it will cause overflow.
    // Therefore, we can consider initializing the number to 10^9 * 10^5 = -10^16 
    // TC: O(nk), SC: O(nk)
    
    static long maximumSum(int n, int k, int p[], int a[], int b[]){
        ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) graph.add(new ArrayList<Integer>());
        for (int i = 0; i < n; i++) {
            if (p[i] > 0) {
                graph.get(p[i] - 1).add(i);
            }
        }
        
        long inf = (long)1e16;
        long[][][] dp = new long[n][2][k];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < 2; j++) {
                for (int l = 0; l < k; l++) {
                    dp[i][j][l] = -inf;
                }
            }
        }
        
        dp[0][0][0] = a[0];
        dp[0][1][0] = b[0];
        return dfs(0, k, graph, a, b, dp);
    }
    
    static long dfs(int node, int k, ArrayList<ArrayList<Integer>> graph, int a[], int b[], long[][][] dp) {
        for (int child : graph.get(node)) {
            for (int i = 0; i < k - 1; i++) {
                dp[child][0][i + 1] = Math.max(dp[child][0][i + 1], a[child] + dp[node][0][i]);
                dp[child][1][i + 1] = Math.max(dp[child][1][i + 1], b[child] + dp[node][1][i]);
            }
            
            for (int i = 0; i < k; i++) {
                dp[child][0][0] = Math.max(dp[child][0][0], a[child] + dp[node][1][i]);
                dp[child][1][0] = Math.max(dp[child][1][0], b[child] + dp[node][0][i]);
            }
        }
        
        long res = Long.MIN_VALUE;
        if (graph.get(node).size() == 0) {
            for (int j = 0; j < k; j++) {
                res = Math.max(res, Math.max(dp[node][0][j], dp[node][1][j]));
            }
        } else {
            for (int child: graph.get(node)) {
                res = Math.max(res, dfs(child, k, graph, a, b, dp));
            }    
        }
        
        return res;
    }
}