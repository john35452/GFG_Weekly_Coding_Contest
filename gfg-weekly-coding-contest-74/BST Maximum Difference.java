

//User function Template for Java

class Solution
{
    // Version 1: Find target number and get the minimum path sum from the target node
    // The difference in this problem is sum - path_sum rather than abs(sum - path_sum)
    // Therefore, we can just focus on minimum path sum.
    // TC: O(h) = O(n), SC: O(n)
    public static int maxDifferenceBST(Node root,int target)
    {
        //Please code here
        int sum = 0;
        boolean found = false;
        Node current = root;
        while(current != null) {
            if (current.data == target) {
                found = true;
                break;
            }
            sum += current.data;
            if (current.data > target) {
                current = current.left;
            } else {
                current = current.right;
            }
        }
        
        if (!found) return -1;
        int[] res = getValue(current);
        res[0] -= current.data;
        res[1] -= current.data;
        
        int ans = Integer.MIN_VALUE;
        if (res[0] != Integer.MAX_VALUE) {
            ans = Math.max(ans, sum - res[0]);
        }
        
        if (res[1] != 0) {
            ans = Math.max(ans, sum - res[1]);
        }
        
        return ans;
    }
    
    public static int[] getValue(Node node) {
        if (node == null) return new int[] {Integer.MAX_VALUE, 0};
        int[] res = new int[] {Integer.MAX_VALUE, 0};
        int[] left = getValue(node.left);
        int[] right = getValue(node.right);
            
        res[0] = Math.min(res[0], Math.min(left[0], right[0]));
        res[1] = Math.max(res[1], Math.max(left[1], right[1]));
        
        if (res[0] == Integer.MAX_VALUE) res[0] = 0;
        res[0] += node.data;
        res[1] += node.data;
        
        return res;
    }
}