

//User function Template for Java

class Solution{
    // Version 1: Try with all subarrays
    // TC: O(n^2), SC: O(1)
    /*
    public long totalSubarrays(long a[], int n, long x){
        // Code Here.
        long ans = 0;
        for (int i = 0; i < n; i++) {
            long res = a[i];
            for (int j = i; j < n; j++) {
                res &= a[j];
                if (res == x) ans += 1;
                else if ((res & x) != x) break;
            }
        }
        return ans;
    }   
    */
    
    // Version 2: Prefix sum of each bit
    // Whenever we meet a number val & x == x, 
    // it's possible to have a valid substring starting from this number.
    // Then we need to consider bits contribute x and bits don't.
    // We can use binary search with prefix sum to search index with consecutive 1 from the number.
    // For the minimum length among all bits contribute to x,
    // it means all substring starting from the number within this length can have and result with x.
    // However, we also need to consider about the bits don't contribute to x.
    // We need to get the maximum length among all bits not contribute to x.
    // Since all substring starting from the number within that length would have and result with other bits which we don't want.
    // As a result, only max(leng_x - lang_nx, 0) substrings are valid.
    // TC: O(32nlogn) = O(nlogn), SC: O(n)
    /*
    public long totalSubarrays(long a[], int n, long x){
        // Code Here.
        long ans = 0;
        int bit[][] = new int[32][n + 1];
        for (int i = 0; i < 32; i++) {
            for (int j = 0; j < n; j++) {
                if ((a[j] & (1<<i)) > 0) {
                    bit[i][j + 1]++;
                    bit[i][j + 1] += bit[i][j];
                }
            }
        }
        
        for (int i = 0; i < n; i++) {
            if ((a[i] & x) == x) {
                int leng_x = Integer.MAX_VALUE;
                int leng_nx = 0;
                for (int j = 0; j < 32; j++) {
                    if ((a[i] & (1<<j)) > 0) {
                        int l = i, m, r = n - 1;
                        while (l < r) {
                            m = l + (r - l) / 2;
                            if (bit[j][m + 1] - bit[j][i + 1] != m - i) {
                                r = m;
                            } else {
                                l = m + 1;
                            }
                        }
                        if (bit[j][l + 1] - bit[j][i + 1] != l - i) l--;
                        if ((x & (1<<j)) > 0) {
                            leng_x = Math.min(leng_x, l - i + 1);
                        } else {
                            leng_nx = Math.max(leng_nx, l - i + 1);
                        }
                    }
                }
                ans += Math.max(leng_x - leng_nx, 0);
            }
        }
        return ans;
    }
    */
    
    // Version 3: DP
    // We can store all possible and result ending at every number.
    // Since in each round, we will & all results with new number, the number of numbers will be limited by this.
    // Therefore, the remaining numbers are the subset of the new number in terms of bits.
    // Since it will get filtered everytime, there will at most 32 numbers remaining in the result set.
    // TC: O(32n) = O(n), SC: O(32) = O(1)
    public long totalSubarrays(long a[], int n, long x){
        // Code Here.
        long ans = 0;
        Map<Long, Long> cur = new HashMap<>();
        Map<Long, Long> prev = new HashMap<>();
        for (long val: a) {
            if ((val & x) == x) {
                prev.put(val, prev.getOrDefault(val, 0L) + 1);
                for (Map.Entry<Long, Long> entry: prev.entrySet()) {
                    long newValue = cur.getOrDefault(entry.getKey() & val, 0L) + entry.getValue();
                    cur.put((entry.getKey() & val), newValue);
                }
                ans += cur.getOrDefault(x, 0L);
            }
            Map<Long, Long> tmp = cur;
            cur = prev;
            prev = tmp;
            cur.clear();
        }        
        return ans;
    }
}