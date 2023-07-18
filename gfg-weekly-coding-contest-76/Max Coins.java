

//User function Template for Java
class Solution{
    // Version 1: Heap 
    // Get the maximum coin we can get by all ranges before current time
    // TC: O(nlogn), SC: O(n)
    /*
    public static int maxCoins(int n,int ranges[][])
    {
        Arrays.sort(ranges, ((a, b) -> Arrays.compare(a, b)));
        PriorityQueue<int[]> pq = new PriorityQueue<int[]> ((a, b) -> Integer.compare(a[0], b[0]));
        int maxv = 0, ans = 0;
        for (int[] interval: ranges) {
            while (!pq.isEmpty() && pq.peek()[0] <= interval[0]) {
                maxv = Math.max(maxv, pq.peek()[1]);
                pq.poll();
            }
            ans = Math.max(ans, interval[2] + maxv);
            pq.offer(new int[] {interval[1], interval[2]});
        }
        return ans;
    }
    */
    
    // Version 2: DP
    // Use binary search to find the location before the range
    // We only can search within the ranges before the current range
    // otherwise it will cause wrong answer
    // TC: O(nlogn), SC: O(n)
    public static int maxCoins(int n,int ranges[][])
    {
        Arrays.sort(ranges, 
            ((a, b) -> (a[1] == b[1]? Integer.compare(a[0], b[0]): 
                        Integer.compare(a[1], b[1]))));
        int[] dp = new int[n + 1];
        Arrays.fill(dp, 0);
        int maxv = 0, ans = 0;
        for (int i = 0; i < n; i++) {
            dp[i + 1] = dp[i];
            int l = 0, r = i, m;
            while (l < r) {
                m = l + (r - l) / 2;
                if (ranges[m][1] > ranges[i][0]) {
                    r = m;
                } else {
                    l = m + 1;
                }
            }
            int index = l;
            ans = Math.max(ans, dp[index] + ranges[i][2]);
            dp[i + 1] = Math.max(dp[i + 1], ranges[i][2]);
        }
        return ans;
    }
    
    
}