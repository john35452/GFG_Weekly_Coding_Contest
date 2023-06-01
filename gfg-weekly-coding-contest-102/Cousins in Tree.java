

//User function Template for Java

class Solution
{
    // Version 1: BFS
    // TC: O(n), SC: O(n)
    static int findCousinSum(Node root, int key) 
    { 
        // code here.
        Map<Integer, Integer> cousin = new HashMap<>();
        Queue<Node[]> queue = new LinkedList<Node[]>();
        Queue<Node[]> queue2 = new LinkedList<Node[]>();
        queue.add(new Node[] {root, null});
        
        
        while (!queue.isEmpty()) {
            long total = 0;
            int count = queue.size();
            Map<Node, Integer> cos = new HashMap<>();
            for (int i = 0; i < count; i++) {
                Node[] pair = queue.poll();
                total += pair[0].data;
                if (!cos.containsKey(pair[1])) {
                    cos.put(pair[1], 0);
                }
                cos.put(pair[1], cos.get(pair[1]) + pair[0].data);
                queue2.offer(pair);
            }
            
            boolean found = false;
            for (int i = 0; i < count; i++) {
                Node[] pair = queue2.poll();
                Node node = pair[0];
                Node par = pair[1];
                if (node.data == key) {
                    found = true;
                }
                if (cos.size() == 1) {
                    cousin.put(node.data, -1);
                } else {
                    cousin.put(node.data, (int)(total - cos.get(par)));
                }
                
                if (node.left != null) {
                    queue.add(new Node[]{node.left, node});
                }
                if (node.right != null) {
                    queue.add(new Node[]{node.right, node});
                }
            }
            
            if (found) {
                break;
            }
        }
        return cousin.get(key);
        
    } 
}