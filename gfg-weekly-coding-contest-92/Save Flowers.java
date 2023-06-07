

//User function Template for Java

class Solution{
    // Version 1: DP
    // dp[i][0 or 1]: The maximum number of flowers can be saved with or without lid be shifted in a[i:]
    // TC: O(n), SC: O(n)
    /*
    public int saveFlowers(int n, int a[], String s){
        // Code Here.
        int ans = 0;
        Integer[][] dp = new Integer[n][2];
        return save(0, 0, a, s, dp);
    }
    
    int save(int index, int moved, int a[], String s, Integer[][] dp) {
        if (index == a.length) {
            return 0;
        } else if (dp[index][moved] == null) {
            int res = 0;
            if (s.charAt(index) == '0' || (s.charAt(index) == '1' && moved > 0)) {
                res = Math.max(res, save(index + 1, 0, a, s, dp));
            }
            if (s.charAt(index) == '1' && moved == 0) {
                res = Math.max(res, a[index] + save(index + 1, 0, a, s, dp));
            }
            if (index + 1 < a.length && s.charAt(index + 1) == '1') {
                if ((s.charAt(index) == '1' && moved > 0) || (s.charAt(index) == '0')) {
                    res = Math.max(res, a[index] + save(index + 1, 1, a, s, dp));
                }
            }
            dp[index][moved] = res;
        }
        return dp[index][moved];
    }
    */
    
    // Version 2: Greedy
    // We can start in revered direction because the lid only can be shifted to left hand side.
    // When we meet lid, we can include one more number before consecutive 1, and drop the minimum value among them.
    // Because we can shift all lids staring from that number to the left hand side.
    // For the ending part, since we cannot shift, we can need to add sum to the final result.
    // TC: O(n), SC: O(1)
    public int saveFlowers(int n, int a[], String s){
        // Code Here.
        int ans = 0;
        int minv = Integer.MAX_VALUE;
        boolean hasLid = false;
        int sum = 0;
        for (int i = n - 1; i >= 0; i--) {
            if (s.charAt(i) == '1') {
                hasLid = true;
                minv = Math.min(minv, a[i]);
                sum += a[i];
            } else {
                if (hasLid) {
                    minv = Math.min(minv, a[i]);
                    sum += a[i];
                    hasLid = false;
                    ans += sum - minv;
                    sum = 0;
                    minv = Integer.MAX_VALUE;
                }
            }
        }
        if (hasLid) {
            ans += sum;
        }
        return ans;
    }
    
}