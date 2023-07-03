//User function Template for C++

class Solution{
    public:
    // Version 1: Greedy
    // Sort by start time, and choose the earliest deadline friends
    // TC: O(nlogn + max(end) * logn), SC: O(n)
    int friends(int N, int K, vector<int> start, vector<int> end){
        // code here
        vector<pair<int, int>> f;
        for (int i = 0; i < N; i++) {
            f.push_back({start[i], end[i]});
        }
        sort(f.begin(), f.end());
        int ans = 0;
        int current = f[0].first;
        int i = 0;
        priority_queue<int, vector<int>, greater<int>> pq;
        while (i < N || !pq.empty()) {
            while (i < N && f[i].first == current) {
                pq.push(f[i].second);
                i++;
            }
            while (!pq.empty() && pq.top() < current) {
                pq.pop();
            }
            
            int count = 0;
            while (!pq.empty() && count < K) {
                ans++;
                count++;
                pq.pop();
            }
            current++;
        }
        return ans;
    }
};