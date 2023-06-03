//User function Template for Java

class Solution{
    // Version 1: Count the number of 1 in binary representation from both side.
    // TC: O(logn), SC: O(logn)
    /*
    public int count101(long n){
        // Code Here
        ArrayList<Integer> num = new ArrayList<>();
        while (n > 0) {
            num.add((int)(n & 1));
            n >>= 1;
        }
        Collections.reverse(num);
        int m = num.size();
        int[] left = new int[m];
        int[] right = new int[m];
        for (int i = 0; i < m; i++) {
            left[i] = num.get(i);
            right[i] = num.get(i);
        }
        
        for (int i = 1; i < m; i++) {
            left[i] += left[i - 1];
            right[m - 1 - i] += right[m - i]; 
        }
        
        int ans = 0;
        for (int i = 1; i < m - 1; i++) {
            if (num.get(i) == 0) {
                ans += left[i] * right[i];
            }
        }
        
        return ans;
    }
    */
    
    // Version 2: Use top down DP to count 101
    // TC: O(logn), SC: O(logn)
    public int count101(long n){
        // Code Here
        ArrayList<Integer> num = new ArrayList<>();
        while (n > 0) {
            num.add((int)(n & 1));
            n >>= 1;
        }
        Collections.reverse(num);
        int m = num.size();
        Integer[][] dp = new Integer[m][3];
        return pick(0, 0, num, dp);
    }
    
    int pick(int i, int j, ArrayList<Integer> num, Integer[][] dp) {
        if (j == 3) {
            return 1;
        } else if (i == num.size()) {
            return 0;
        }
        if (dp[i][j] == null) {
            int res = pick(i + 1, j, num, dp);
            if (num.get(i) == ((j % 2 == 0)? 1 : 0)) {
                res += pick(i + 1, j + 1, num, dp);
            }
            dp[i][j] = res;
        }
        return dp[i][j];
    }
}