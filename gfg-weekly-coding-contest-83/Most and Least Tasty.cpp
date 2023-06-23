//User function Template for C++

class Solution{
    public:
    // Version 1: DP(TLE)
    // Use dp to calculate the maximum and minimum value
    // TC: O(nk), SC: O(nk)
    /*
    long long diffInTaste(int N, int K, int Arr[])
    {
        // code here
        vector<vector<long long>> maxv(N, vector<long long>(K + 1, -1));
        vector<vector<long long>> minv(N, vector<long long>(K + 1, -1));
        return getMax(0, 0, K, maxv, Arr) - getMin(0, 0, K, minv, Arr);
    }
    
    long long getMax(int last_index, int index, int remain, vector<vector<long long>>& maxv, int Arr[]) {
        if (index == maxv.size()) {
            if (remain == 0) return 0;
            else return LLONG_MIN;
        }
        else if (maxv[index][remain] >= 0) {
            return maxv[index][remain];
        }
        
        long long res = LLONG_MIN;
        if (remain > 0) {
            for (int i = index; i < maxv.size(); i++) {
                res = max(res, Arr[last_index] + Arr[i] + getMax(i + 1, i + 1, remain - 1, maxv, Arr));
            }    
        }
        maxv[index][remain] = res;
        return maxv[index][remain];
        
    }
    
    long long getMin(int last_index, int index, int remain, vector<vector<long long>>& minv, int Arr[]) {
        if (index == minv.size()) {
            if (remain == 0) return 0;
            else return pow(10, 10);
        }
        else if (minv[index][remain] >= 0) {
            return minv[index][remain];
        }
        
        long long res = pow(10, 10);
        if (remain > 0) {
            for (int i = index; i < minv.size(); i++) {
                res = min(res, Arr[last_index] + Arr[i] + getMin(i + 1, i + 1, remain - 1, minv, Arr));
            }    
        }
        minv[index][remain] = res;
        return minv[index][remain];
    }
    */
    
    // Version 2: Max and Min k
    // For a partition arr[l], arr[r], if we choose this arr[r + 1] will also be chosen.
    // We know arr[0] and arr[n - 1] will be chosen.
    // Therefore, the total taste will be arr[0] + arr[n - 1] with k - 1 pair for arr[i] + arr[i + 1].
    // Therefore, we can get the maximum and minimum k pair.
    // TC: O(nlogn), SC: O(n)
    /*
    long long diffInTaste(int N, int K, int Arr[])
    {
        // code here
        priority_queue<long long> maxv;
        priority_queue<long long, vector<long long>, greater<long long>> minv;
        
        for (int i = 0; i < N - 1; i++) {
            maxv.push((long)(Arr[i] + Arr[i + 1]));
            minv.push((long)(Arr[i] + Arr[i + 1]));
        }
        
        long long ans = 0;
        for (int i = 0; i < K - 1; i++) {
            ans += maxv.top();
            ans -= minv.top();
            maxv.pop();
            minv.pop();
        }
        return ans;
    }
    */
    
    // Version 3: Improved version 2
    // Use min-heap for maximum pair, max-heap for minimum pair.
    // TC: O(nlogk), SC: O(k)
    long long diffInTaste(int N, int K, int Arr[])
    {
        // code here
        priority_queue<long long> minv;
        priority_queue<long long, vector<long long>, greater<long long>> maxv;
        
        for (int i = 0; i < N - 1; i++) {
            maxv.push((long)(Arr[i] + Arr[i + 1]));
            minv.push((long)(Arr[i] + Arr[i + 1]));
            if (maxv.size() > K - 1) maxv.pop();
            if (minv.size() > K - 1) minv.pop();
        }
        
        
        long long ans = 0;
        for (int i = 0; i < K - 1; i++) {
            ans += maxv.top();
            ans -= minv.top();
            //cout << maxv.top() << " " << minv.top() << endl;
            maxv.pop();
            minv.pop();
        }
        return ans;
    }
};