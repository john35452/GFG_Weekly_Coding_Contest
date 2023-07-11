

class Solution {
    // Version 1: Top down DP
    // dp[i][bal][j][pre]: The number of distinct valid string we can find 
    // starting from index i, balance bal, j consecutive bucket and pre as the last character.
    // TC: O(n^2 * k), SC: O(n^2 * k)
    public static int countStrings(int n, String s, int k) {
        // code here
        Long dp[][][][] = new Long[n][n][k + 1][2];
        long M = (long)Math.pow(10, 9) + 7;
        return (int)compute(0, 0, 0, 0, s, k, M, dp);
    }
    
    public static long compute(int index, int balance, int cnt, int pre, String s,
        int k, long M, Long[][][][] dp) {
        if (cnt > k || balance < 0) return 0;
        else if (index == s.length()) return balance == 0 ? 1: 0;
        else if (s.charAt(index) == '(') {
            int nextCnt;
            if (pre == 0) {
                nextCnt = cnt + 1;
            } else {
                nextCnt = 1;
            }
            return compute(index + 1, balance + 1, nextCnt, 0, s, k, M, dp);
        } else if (s.charAt(index) == ')') {
            int nextCnt;
            if (pre == 1) {
                nextCnt = cnt + 1;
            } else {
                nextCnt = 1;
            }
            return compute(index + 1, balance - 1, nextCnt, 1, s, k, M, dp);
        }
        else if (dp[index][balance][cnt][pre] != null) return dp[index][balance][cnt][pre];
        else {
            long res = 0;
            if (pre == 0) {
                res = compute(index + 1, balance + 1, cnt + 1, 0, s, k, M, dp);
                res = (res + compute(index + 1, balance - 1, 1, 1, s, k, M, dp)) % M;
            } else {
                res = compute(index + 1, balance - 1, cnt + 1, 1, s, k, M, dp);
                res = (res + compute(index + 1, balance + 1, 1, 0, s, k, M, dp)) % M;
            }
            dp[index][balance][cnt][pre] = res;
            return dp[index][balance][cnt][pre];
        }
    }
}
        