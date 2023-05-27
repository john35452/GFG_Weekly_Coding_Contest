//User function Template for Java

class Solution{
    // Version 1: Sort
    // TC: O(nlogn), SC: O(1)
    public long maximumSum(int A[], int n){
        // Code Here.
        Arrays.sort(A);
        long ans = 0;
        for (int i = 0; i < n; i++) {
            ans += 1L * (i + 1) * A[i];
        }
        return ans;
    }
}