

class Solution{
    // Version 1: Count
    // TC: O(n), SC: O(1)
    public int separateStones(int N, int K, int arr[]) {
        // Code Here.
        int zero = 0, one = 0;
        for (int i = 0; i < N; i++) {
            if (arr[i] == 0) zero++;
            else one++;
        }
        return (int)Math.ceil(1.0 *zero / K) + (int)Math.ceil(1.0 * one / K);
    }
    
}