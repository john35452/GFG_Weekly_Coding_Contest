

//User function Template for Java

class Solution{
    // Version 1: Prefix sum
    // Store difference for each price range, and go through them once to know overlapping count for each time
    // Check whether the time is valid, and calculate the presum sum of the result.
    // TC: O(n + q + max(price, queries)), SC: O(max(price, queries))
    static int[] bestPrice(int n,int price[][],int k,int q,int queries[][]){
        int maxv = 0;
        for (int i = 0; i < n; i++) {
            maxv = Math.max(maxv, price[i][1]);
        }
        
        for (int i = 0; i < q; i++) {
            maxv = Math.max(maxv, queries[i][1]);
        }
        
        int diff[] = new int[maxv + 2];
        for (int[] pair : price) {
            diff[pair[0]] += 1;
            diff[pair[1] + 1] -= 1;
        }
        
        int prefix[] = new int[maxv + 2];
        int current = 0;
        for (int i = 0; i <= maxv; i++) {
            current += diff[i];
            prefix[i + 1] = prefix[i] + ((current >= k) ? 1: 0);
        }
        
        int ans[] = new int[q];
        for (int i = 0; i < q; i++) {
            ans[i] = prefix[queries[i][1] + 1] - prefix[queries[i][0]];
        }
        return ans;
    }
}