

//User function Template for Java

class Solution{
    // Version 1: Greedy and cases
    // Connect all nodes to the root
    // Check three cases for root
    // Root val:
    // 1. 0
    // 2. minv
    // 3. Original value
    // TC: O(n), SC: O(1)
    public long solve(int N, int Par[], int Arr[], int K, int A, int B){
        // Code Here.
        if (A > B) {
            A = B;
        }
        
        int root = -1;
        long ans = Long.MAX_VALUE;
        long minv = Long.MAX_VALUE;
        for (int i = 0; i < N; i++) {
            if (Par[i] == -1) {
                root = i;
            } 
            minv = Math.min(minv, Arr[i]);
        }
        
        long score1 = B;
        for (int i = 0; i < N; i++) {
            if (i != root) {
                if (Arr[i] > K) {
                    score1 += A;
                }
            }
        }
        ans = Math.min(ans, score1);
        
        if (minv <= K) {
            long score2 = A;
            for (int i = 0; i < N; i++) {
                if (i != root) {
                    if (Arr[i] + minv > K) {
                        if (2 * minv <= K) {
                            score2 += A;
                        } else {
                            score2 += B;
                        }
                    }
                }
            }
            ans = Math.min(ans, score2);
        }
        
        if (Arr[root] <= K) {
            long score3 = 0;
            for (int i = 0; i < N; i++) {
                if (i != root) {
                    if (Arr[root] + Arr[i] > K) {
                        if (Arr[root] + minv <= K) {
                            score3 += A;
                        } else {
                            score3 += B;
                        }
                    }
                }
            }
            ans = Math.min(ans, score3);
        }
        return ans;
    }
}