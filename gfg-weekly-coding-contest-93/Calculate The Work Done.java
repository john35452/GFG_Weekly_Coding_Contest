

//User function Template for Java

class Solution{
    // Version 1: Set + Queue
    // TC: O(n), SC: O(cap)
    public int workDone(int n, int a[], int cap){
        // Code Here. 
        Set<Integer> curSet = new HashSet<>();
        Deque<Integer> belt = new ArrayDeque<>();
        int ans = 0;
        for (int i = 0; i < n; i++) {
            if (!curSet.contains(a[i])) {
                belt.offerFirst(a[i]);
                curSet.add(a[i]);
                ans += 1;
                if (belt.size() > cap) {
                    int val = belt.pollLast();
                    curSet.remove(Integer.valueOf(val));
                }
            } 
        }
        return ans;
    }
}