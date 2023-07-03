
class Solution {
  public:
    // Version 1: Hashmap
    // pre[val][count]: The number of val with count times of X until now
    // TC: O(n), SC: O(n)
    /*
    long long countSubarray(int N, vector<int> &arr, int X, int K) {
        // code here
        unordered_map<int, unordered_map<int, int>> pre;
        pre[X][0] = 1;
        long long M = pow(10, 9) + 7;
        long long ans = 0, current = 0;
        for (int i = 0; i < N; i++) {
            current += (arr[i] == X? 1: 0);
            ans = (ans + pre[arr[i]][current - K]) % M;
            pre[arr[i]][current]++;
        }
        return ans;
    }
    */
    
    // Verion 2: Sliding window
    // When we have k X, count the occurrence of non-X numbers from left.
    // Precede the right position until we meet X to count the number of valid substrings
    // TC: O(n), SC: O(n)
    long long countSubarray(int N, vector<int> &arr, int X, int K) {
        long long ans = 0;
        int count = 0;
        int l = 0, r = 0;
        int M = pow(10, 9) + 7;
        while (r < N) {
            if (arr[r] == X) count++;
            r++;
            if (count == K) {
                unordered_map<int, int> pre;
                while(arr[l] != X) {
                    pre[arr[l]]++;
                    l++;
                }
                
                ans = (ans + 1) % M;
                while(r < N && arr[r] != X) {
                    ans = (ans + pre[arr[r]]) % M;
                    r++;
                }
                l++;
                count--;
            }
        }
        return ans;
    }
};