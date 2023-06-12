

//User function Template for Java

/* 
class Node
{
    int data;
    Node left, right;

    Node(int item)
    {
        data = item;
        left = right = null;
    }
} 
*/
class Solution{
    // This is the same question as binary tree cameras on Leetcode
    // https://leetcode.com/problems/binary-tree-cameras/
    // Version 1: Greedy
    // Use post traversal and supply vaccine when needed.
    // TC: O(n), SC: O(n)
    /*
    public static int supplyVaccine(Node root){
        // code here
        Set<Node> covered = new HashSet<>();
        Map<Node, Node> parent = new HashMap<>();
        covered.add(null);
        return dfs(root, null, parent, covered);
        
    }
    
    public static int dfs(Node node, Node p, Map<Node, Node> parent, Set<Node> covered) {
        if (node == null) return 0;
        int res = 0;
        parent.put(node, p);
        res += dfs(node.left, node, parent, covered);
        res += dfs(node.right, node, parent, covered);
        if (!covered.contains(node.left) || !covered.contains(node.right) || (p == null && !covered.contains(node))) {
            covered.add(node);
            covered.add(node.left);
            covered.add(node.right);
            covered.add(p);
            res++;
        }
        return res;
    }
    */
    
    // Version 2: Return the state of the subtree
    // 0: root covered but no camera
    // 1: root covered and with camera
    // 2: root not covered
    // TC: O(n), SC: O(1)
    public static int supplyVaccine(Node root){
        // code here
        int[] ans = new int[1]; 
        if (dfs(root, ans) > 1) {
            ans[0]++;
        }
        return ans[0];
    }
    
    
    public static int dfs(Node node, int[] ans) {
        if (node == null) return 0;
        int left = dfs(node.left, ans);
        int right = dfs(node.right, ans);
        if (left == 2 || right == 2) {
            ans[0]++;
            return 1;
        }
        else if (left == 1 || right == 1) return 0;
        else return 2;
    }
}