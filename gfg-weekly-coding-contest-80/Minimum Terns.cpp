
class Solution {
  public:
    // Version 1: Binary Search
    // Get the number of 1 and 2 refills.
    // We can change one 2 to two 1.
    // Use binary search to find the minimum situation
    // TC: O(log(sum(amount))), SC: O(1)
    /*
    long long minimumTerns(int n, vector<int> &amount) {
        // code here
        int maxv = *max_element(amount.begin(), amount.end());
        long long even = 0, odd = 0, ans = LLONG_MAX;
        for (int i = 0; i < n; i++) {
            int left = maxv - amount[i];
            even += left / 2;
            odd += left % 2;
        }
        if (even > 0 || odd > 0) {
            if (even >= odd) {
                long long l = 0;
                long long r = even;
                while (l < r) {
                    long long m = l + (r - l) / 2;
                    if (odd + 2 * m > even - m) {
                        r = m;
                    } else {
                        l = m + 1;
                    } 
                }
                odd += 2*l;
                even -= l;    
                ans = min(ans, 2 * (even + 1));
            }
            ans = min(ans, 2 * odd - 1);
            return ans;
        } else {
            return 0;
        }
    }
    */
    
    // Version 2: Binary Search
    // Search for the minimum amount of time
    // TC: O(log(sum(amount))), SC: O(1)
    long long minimumTerns(int n, vector<int> &amount) {
        // code here
        int maxv = *max_element(amount.begin(), amount.end());
        long long even = 0, odd = 0, ans = LLONG_MAX;
        for (int i = 0; i < n; i++) {
            int left = maxv - amount[i];
            even += left / 2;
            odd += left % 2;
        }
        
        long long l = 0, r = max(2 * even, 2 * odd - 1);
        while (l < r) {
            long long m = l + (r - l) / 2;
            if (check(m, even, odd)) {
                r = m;
            } else {
                l = m + 1;
            }
        }
        return l;
    }
    
    bool check(long long t, long long even, long long odd) {
        long long even_t = t / 2;
        long long odd_t = (t + 1) / 2;
        if (odd > odd_t) {
            return false;
        }
        even -= even_t;
        if (even > 0) {
            odd += 2 * even;
        }
        return odd_t >= odd;
    }
};