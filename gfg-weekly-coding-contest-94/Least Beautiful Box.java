

//User function Template for Java

class Solution{
    // Version 1: DP
    // data[key] : Store the length of sequences ending at key until now.
    // Always pick the shortest one and add new number to that sequence.
    // Therefore, we need to use heap to store sequences.
    // TC: O(nlogn), SC: (n)
    public int minimumBeauty(int id[], int n){
        // Code Here.
        Arrays.sort(id);
        Map<Integer, PriorityQueue<Integer>> data = new HashMap<>();
        int ans = Integer.MAX_VALUE;
        for (int val: id) {
            if (data.containsKey(val - 1)) {
                int count = data.get(val - 1).poll();
                if (data.get(val - 1).isEmpty()) {
                    data.remove(val - 1);
                }
                data.putIfAbsent(val, new PriorityQueue<Integer>());
                data.get(val).offer(count + 1);
            } else {
                data.putIfAbsent(val, new PriorityQueue<Integer>());
                data.get(val).offer(1);
            }
        }
        for (PriorityQueue<Integer> pq: data.values()) {
            ans = Math.min(ans, pq.peek());
        }
        
        return ans;
    }
}