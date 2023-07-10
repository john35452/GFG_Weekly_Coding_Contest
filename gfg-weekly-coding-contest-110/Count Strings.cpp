//User function Template for C++
const int N = 200;
class Solution{
public:
    // Version 1: Top down DP
    // dp[i][bal][j][pre]: The number of distinct valid string we can find 
    // starting from index i, balance bal, j consecutive bucket and pre as the last character.
    // TC: O(n^2 * k), SC: O(n^2 * k)
    long long M = pow(10, 9) + 7;
    long long dp[N][N][11][2];
    int countStrings(int n,string &s,int k){
        memset(dp, -1, sizeof(dp));
        return (int)compute(0, 0, 0, 0, n, k, s);
    }
    
    long long compute(int index, int balance, int cnt, int pre, int n, int k, string &s) {
        if (balance < 0 || cnt > k) return 0;
        else if (index == n) return balance == 0 ? 1: 0;
        else if (s[index] == '(') {
            int nextCnt;
            if (pre == 0) {
                nextCnt = cnt + 1;
            } else {
                nextCnt = 1;
            }
            return compute(index + 1, balance + 1, nextCnt, 0, n, k, s);
        } else if (s[index] == ')') {
          int nextCnt;
          if (pre == 1) {
              nextCnt = cnt + 1;
          } else {
              nextCnt = 1;
          }
          return compute(index + 1, balance - 1, nextCnt, 1, n, k, s);
        } else if (dp[index][balance][cnt][pre] >= 0) {
            return dp[index][balance][cnt][pre];
        } else {
            long long res = 0;
            if (pre == 0) {
                res = (compute(index + 1, balance + 1, cnt + 1, 0, n, k, s) + 
                    compute(index + 1, balance - 1, 1, 1, n, k, s)) % M;
            } else {
                res = (compute(index + 1, balance - 1, cnt + 1, 1, n, k, s) + 
                    compute(index + 1, balance + 1, 1, 0, n, k, s)) % M;
            }
            dp[index][balance][cnt][pre] = res;
            return dp[index][balance][cnt][pre];    
        }
        
    }
};