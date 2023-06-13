class Solution {
  public:
    // Version 1: GCD
    // The maximum size of the bucket is the GCD of all arr[i]
    // TC: O(n * log(max(arr))), SC: O(1)
    long long minimumBuckets(int N, vector<int> &arr) {
        // code here
        long long ans = 0;
        int g = arr[0];
        for (int i = 1; i < arr.size(); i++) {
            g = gcd(g, arr[i]);
        }
        
        for (int i = 0; i < arr.size(); i++) {
            ans += arr[i] / g;
        }
        return ans;
    }
    
    int gcd(int a, int b) {
        if (b == 0) return a;
        else return gcd(b, a % b);
    }
};