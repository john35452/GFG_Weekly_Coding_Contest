

class Solution{
    // Version 1: Check cycle size
    // There is no way to reproduce a cycle with size n
    // Therefore, if any node is not included in the cycle, the length of cycle is not n.
    // We can check whether any node's outgoing edge count is 1 
    // which means this node is not included in the cycle.
    // TC: O(V) = O(n), SC: O(n)
    public String cyclicTree(int n, int edges[][]){
        // Code Here. 
        ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) graph.add(new ArrayList<Integer>());
        
        for (int i = 0; i < edges.length ; i++) {
            graph.get(edges[i][0] - 1).add(edges[i][1] - 1);
            graph.get(edges[i][1] - 1).add(edges[i][0] - 1);
        }
        
        for (int i = 0; i < n; i++) {
            if (graph.get(i).size() == 1) return "Yes";
        }
        return "No";
    }
    
}