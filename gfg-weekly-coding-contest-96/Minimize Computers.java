//User function Template for Java

class Solution{
    // Version 1: Binary Search
    // We can use min heap to know when will a seat can be released.
    // It takes O(nlogn) for each check.
    // TC: O(nlogn * logn), SC: O(n)
    public int minimizeComputers(int arr[], int n, int k){
        // Code Here.
        int l = 1, r = n, m;
        while (l < r) {
            m = l + (r - l) / 2;
            if (run(m, arr) <= k) {
                r = m;
            } else {
                l = m + 1;
            }
        }
        return l;
    }
    
    public int run(int seat, int arr[]) {
        int end, res = 0;
        int i = 0;
        PriorityQueue<Integer> option = new PriorityQueue<>();
        for (i = 0; i < seat; i++) {
            option.offer(arr[i]);
        }
        i = seat;
        while (!option.isEmpty()) {
            end = option.poll();
            res = Math.max(res, end);
            if (i < arr.length) {
                option.offer(end + arr[i]);
                i += 1;
            }
        }
        return res;
    }
}