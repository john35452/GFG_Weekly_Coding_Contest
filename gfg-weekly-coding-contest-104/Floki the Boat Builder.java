

//User function Template for Java

class Solution
{
    // Version 1: GCD and DP
    // If the LCA of x and y is x or y, they are in the same subtree.
    // We can store the subtree gcd in a list and use them later.
    // We can use DFS to find LCA and fill in the result list of gcd subtree.
    // TC: O(nlog(max(val)), SC: O(n)
	public int gcdTree(int n, ArrayList<ArrayList<Integer> > edges, ArrayList<Integer> val , int x, int y)
	{
		// code here
		ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
		for (int i = 0; i < n; i++) {
		    graph.add(new ArrayList<Integer>());
		}
		
		for (ArrayList<Integer> e : edges) {
		    graph.get(e.get(0)).add(e.get(1));
		    graph.get(e.get(1)).add(e.get(0));
		}
		
		int[] gcd = new int[n];
		ArrayList<Integer> lca = new ArrayList<>();
		dfs(0, -1, graph, gcd, lca, val, x, y);
		
		if (lca.get(0) == x || lca.get(0) == y) {
		    return -1;
		} else {
		    return _gcd(gcd[x], gcd[y]);
		}
	}
	
	int _gcd(int a, int b) {
	    if (b == 0) {
	        return a;
	    } else {
	        return _gcd(b, a % b);
	    }
	}
	
	int[] dfs(int node, int parent, ArrayList<ArrayList<Integer>> graph, int[] gcd, ArrayList<Integer> LCA, ArrayList<Integer> val, int x, int y) {
	    int g = val.get(node);
	    int count = 0;
	    if (node == x || node == y) {
	        count += 1;
	    }
	    for (int child : graph.get(node)) {
	        if (child != parent) {
	            int[] res = dfs(child, node, graph, gcd, LCA, val, x, y);
	            count += res[0];
	            g = _gcd(g, res[1]);
	        }
	    }
	    if (count == 2) {
	        if (LCA.size() == 0) {
	            LCA.add(node);
	        }
	    }
	    gcd[node] = g;
	    return new int[]{count, g};
	}
}
	  