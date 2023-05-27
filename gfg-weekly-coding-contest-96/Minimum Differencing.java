//User function Template for Java

class Solution{
    // Version 1: Greedy
    // Only odd number have the chance to become bigger, and since k is even,
    // so they only have one chance to become greater.
    // We can multiple all odd number by k, then all numbers go toward the same direction.
    // At this moment, we can memorize the minimum value and use a max-heap to trace the current max value.
    // We always divide the maximum value in the heap and update the current minimin value.
    // Whenever we meet a odd number, the process should stop because our maximum value is fixed now.
    // Note: Let v be the range of arr[i].
    // TC: O(log(max(arr)) * nlogn), SC: O(n)
    public int minimizeDifference(int arr[], int n, int k){
        // Code Here.
        long minv = Long.MAX_VALUE, ans = Long.MAX_VALUE, val;
        PriorityQueue<Long> pq = new PriorityQueue<>((a, b) -> Long.compare(b, a));
        for (int i = 0; i < n; i++) {
            if (arr[i] % 2 > 0) {
                val = 1L * arr[i] * k;
            } else {
                val = 1L * arr[i];
            }
            pq.offer(val);
            minv = Math.min(minv, val);
        }
        
        while (pq.peek() % 2 == 0) {
            val = pq.peek();
            ans = Math.min(ans, val - minv);
            
            if (val % 2 == 0) {
                pq.poll();
                pq.offer(val / 2);
                minv = Math.min(minv, val / 2);
            } else {
                break;
            }
        }
        ans = Math.min(ans, pq.peek() - minv);
        return (int)ans;
    }
}