

//User function Template for Java

class Solution{
    // Version 1: Try with all combination
    // Use bitmask to represent whether to take each course
    // TC: O(2^n * (n + m)), SC: O(m)
    public int minimumCost(int n, int m, int x, int p[], int a[][]){
        // Code Here.
        if (m == 0) return (x == 0 ? 0: -1);
        int ans = Integer.MAX_VALUE;
        int score[] = new int[m];
        for (int mask = 0; mask < 1<<n; mask ++) {
            Arrays.fill(score, 0);
            int price = 0;
            for (int i = 0; i < n; i++) {
                if ((mask & (1<<i)) > 0) {
                    price += p[i];
                    for (int j = 0; j < m; j++) {
                        score[j] += a[i][j];
                    }
                }
            }
            boolean done = true;
            for (int j = 0; j < m; j++) {
                if (score[j] < x) {
                    done = false;
                    break;
                } 
            }
            if (done) {
                ans = Math.min(ans, price);
            }
        }
        if (ans == Integer.MAX_VALUE) return -1;
        else return ans;
    }   

}