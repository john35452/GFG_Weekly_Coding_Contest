//User function Template for C++
class Solution{
public:
    // Version 1: Use prefix to calculate cost for each index
    // Let say index is 1.
    // The cost is arr[0] * 1 + arr[1] * 0 + arr[2] * 1 + ...+ arr[n - 1] * (n - 2)
    // The cost for index 2 is as below.
    // arr[0] * 2 + arr[1] * 1 + arr[2] * 0 + arr[3] * 1 + ...+ arr[n - 1] * (n - 3)
    // The difference is (arr[0] + arr[1]) - (arr[2] + arr[3] + ... + arr[n - 1])
    // Therefore, we can use prefix sum to adjust from one index to another.
    // TC: O(n), SC: O(n)
    long long MinCost(int n, int weightsArr[]){
        long long current = 0;
        for (int i = 1; i < n; i++) {
            current += i * weightsArr[i];
            weightsArr[i] += weightsArr[i - 1];
        }
        
        long long ans = current;
        for (int i = 0; i < n; i++) {
            current += weightsArr[i];
            current -= weightsArr[n - 1] - weightsArr[i];
            ans = min(ans, current);
        }
        return ans;
    }
};