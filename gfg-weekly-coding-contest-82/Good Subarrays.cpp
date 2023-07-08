//User function Template for C++

class Solution {
  public:
    // Version 1: Sliding window
    // Use sliding window to get the number of subarray with at most k elements occurred at least 3 times
    // TC: O(n), SC: O(1)
    long long goodSubarrays(int n,int x, vector<int>arr) {
        // code here
        return atmostk(x, arr) - atmostk(x - 1, arr);
    }
    
    long long atmostk(int k, vector<int>& arr) {
        unordered_map<int, int> fre;
        int l = 0, match = 0;
        long long ans = 0;
        for (int r = 0; r < arr.size(); r++) {
            if (fre.find(arr[r]) == fre.end()) {
                fre[arr[r]] = 0;
            }
            fre[arr[r]]++;
            if (fre[arr[r]] == 3) match++;
            while (match > k) {
                if (fre[arr[l]] == 3) match--;
                fre[arr[l]]--;
                l++;
            }
            ans += (r - l + 1);
        }
        return ans;
    }
};
