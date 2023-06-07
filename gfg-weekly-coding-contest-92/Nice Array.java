

//User function Template for Java

class Solution{
    // Version 1: Count consecutive numbers
    // TC: O(n), SC: O(1)
    public int niceSubarray(int a[], int n){
        // Code Here.
        int ans = 0;
        int current = 0;
        for (int i = 0; i < n; i++) {
            if (a[i] == current) {
                current += 1;
            } else {
                ans = Math.max(ans, current - 1);
                if (a[i] == 1) {
                    current = 2;
                } else {
                    current = 1;
                }
            }
        }
        ans = Math.max(ans, current - 1);
        return ans;
    }
}