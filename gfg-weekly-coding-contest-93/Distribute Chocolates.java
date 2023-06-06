

//User function Template for Java

class Solution{
    // Version 1: Binary Search
    // TC: O(nlog(max(a)), SC: O(1) 
    public int maxChocolates(int a[], int n, int M){
        // Code Here.
        int l = 1, r = Arrays.stream(a).max().getAsInt();
        while (l < r) {
            int m = l + (r - l) / 2;
            if (!check(m, M, a)) {
                r = m;
            } else {
                l = m + 1;
            }
        }
        return l - (check(l, M, a)? 0:1);
    }
    
    boolean check(int candies, int M, int amount[]) {
        int student = 0;
        for (int i = 0; i < amount.length; i++) {
            student += amount[i] / candies;
        }
        return student >= M;
    }
}