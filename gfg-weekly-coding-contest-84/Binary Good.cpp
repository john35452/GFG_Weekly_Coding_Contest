//User function Template for C++

class Solution
{
    public:
    // Version 1: Median
    // Get the length of all consecutive ones
    // This approach doesn't consider if we remove any group of one.
    // This will cause some wrong answer case.
    // Ex: 010111 and 0101011110
    // TC: O(nlogn), SC: O(n)
    /*
    int solve(string str, int n)
    {
        // add your code here
        vector<int> option;
        int count = 0;
        for (int i = 0; i < n; i++) {
            if (str[i] == '1') {
                count++;
            } else {
                if (count > 0) option.emplace_back(count);
                count = 0;
            }
        }
        if (count > 0) option.emplace_back(count);
        if (option.empty()) return 0;
        sort(option.begin(), option.end());
        int ans = 0;
        int mid = option[option.size() / 2];
        for (int i = 0; i < option.size(); i++) {
            ans += abs(mid - option[i]);
        }
        return ans;
    }
    */
    
    // Version 2: Prefix sum + Median
    // Consider removing groups of one from the smallest group
    // This can deal with the case like 0111110101
    // But the answer for those case are set wrong in the judge, this code will get WA in the judge.
    // TC: O(nlogn), SC: O(n)
    int solve(string str, int n)
    {
        // add your code here
        vector<int> option;
        int count = 0;
        for (int i = 0; i < n; i++) {
            if (str[i] == '1') {
                count++;
            } else {
                if (count > 0) option.emplace_back(count);
                count = 0;
            }
        }
        if (count > 0) option.emplace_back(count);
        if (option.empty()) return 0;
        sort(option.begin(), option.end());
        
        int m = option.size();
        vector<int> prefix(m + 1, 0);
        for (int i = 0; i < m; i++) {
            prefix[i + 1] = prefix[i] + option[i];
        }
        
        int ans = INT_MAX;
        for (int i = 0; i < option.size(); i++) {
            int mid = (i + m - 1) / 2;
            int left = option[mid] * (mid - i) - (prefix[mid] - prefix[i]);
            int right = prefix[m] - prefix[mid] - option[mid] * (m - mid);
            ans = min(ans, prefix[i] + left + right);
        }
        return ans;
    }
};