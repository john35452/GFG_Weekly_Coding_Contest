// User function Template for C++

class Solution
{
public:
    // Version 1: Greedy
    // Store the position of maximum value
    // Consider the number non-maximum value in front of a maximum value.
    // Even: It takes count / 2 to update them.
    // x x x x 5 =>     5 5 5
    //              5 5 5
    // Odd: It taks (count + 1) / 2 to update them
    // and one number after the maximum number will be updated as well.
    // x x x 5 y => 5 5 5
    //                  5 5 5
    // Therefore, we can increase answer by (count + 1) / 2 to update non-maximum numbers.
    // We only need to take care the non-maximum numbers after the last maxium number afterward.
    // TC: O(n), SC: O(n)
    int minimumOperations(int n, vector<int> &arr)
    {
        // code here
        int maxv = *max_element(arr.begin(), arr.end());
        vector<int> pos;
        for (int i = 0; i < n; i++)
        {
            if (arr[i] == maxv)
            {
                pos.push_back(i);
            }
        }
        int ans = 0, l = 0;
        for (int i = 0; i < pos.size(); i++)
        {
            int count = pos[i] - l;
            ans += (count + 1) / 2;
            if (count % 2 > 0)
            {
                l = pos[i] + 2;
            }
            else
            {
                l = pos[i] + 1;
            }
        }
        int count = n - l;
        ans += (count + 1) / 2;
        return ans;
    }
};