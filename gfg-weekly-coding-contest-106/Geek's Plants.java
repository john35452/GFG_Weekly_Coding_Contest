

class Solution{
    // Version 1: GCD
    // The maximum size of the bucket is the GCD of all arr[i]
    // TC: O(n * log(max(arr))), SC: O(1)
    public long minimumBuckets(int N, int arr[]){
        // Code here.
        long g = arr[0];
        for (int i = 1; i < N; i++) {
            g = gcd(g, arr[i]);
        }
        long ans = 0;
        for (int i = 0; i < N; i++) {
            ans += 1L * arr[i] / g;
        }
        return ans;
    }
    
    public long gcd(long a, long b) {
        if (b == 0) return a;
        else return gcd(b, a % b);
    }
}