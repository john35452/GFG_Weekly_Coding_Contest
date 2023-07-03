

//User function Template for Java
class Solution 
{ 
    // Version 1: Greedy
    // Sort by start time, and choose the earliest deadline friends
    // TC: O(nlogn + max(end) * logn), SC: O(n)
    int friends(int N, int K, int start[] ,int end[]) 
    { 
        // code here
        ArrayList<ArrayList<Integer>> f = new ArrayList<ArrayList<Integer>>();
        for (int i = 0; i < N; i++) {
            f.add(new ArrayList<>());
            f.get(i).add(start[i]);
            f.get(i).add(end[i]);
        }
        Collections.sort(f, (l1, l2) -> Integer.compare(l1.get(0), l2.get(0)));
        
        PriorityQueue<Integer> pq = new PriorityQueue<Integer>();
        int i = 0;
        int current = f.get(0).get(0);
        int ans = 0;
        while (i < f.size() || !pq.isEmpty()) {
            while (i < N && f.get(i).get(0) == current) {
                pq.offer(f.get(i).get(1));
                i++;
            }
            
            while (!pq.isEmpty() && pq.peek() < current) {
                pq.poll();
            }
            
            int count = 0;
            while (!pq.isEmpty() && count < K) {
                pq.poll();
                count++;
                ans++;
            }
            current++;
        }
        return ans;
    }
} 