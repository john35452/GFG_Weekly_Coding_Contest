// User function Template for C++

class Solution {
  public:
    // Version 1: BFS
    // TC: O(N + K), SC: O(N)
    /*
    long long solve(int N, int K, vector<long long> GeekNum) {
        // code here
        int m = GeekNum.size();
        deque<long long> d;
        long long current = 0;
        for (int i = 0; i < K; i++) {
            current += GeekNum[m - K + i];
            d.emplace_back(GeekNum[m - K + i]);
        }
        while (GeekNum.size() < N) {
            //cout << GeekNum.size() << " " << current << endl;
            GeekNum.emplace_back(current);
            d.emplace_back(current);
            current *= 2;
            current -= d.front();
            d.pop_front();
        }
        return GeekNum[N - 1];
    }
    */
    
    // Version 2: BFS
    // TC: O(N + K), SC: O(K)
    long long solve(int N, int K, vector<long long> GeekNum) {
        // code here
        int m = GeekNum.size();
        if (N < m) {
            return GeekNum[N - 1];
        }
        deque<long long> d;
        long long current = 0;
        for (int i = 0; i < K; i++) {
            current += GeekNum[m - K + i]; 
            d.emplace_back(GeekNum[m - K + i]);
        }
        for (int i = m; i < N; i++) {
            GeekNum.emplace_back(current);
            d.emplace_back(current);
            current *= 2;
            current -= d.front();
            d.pop_front();
        }
        return d.back();
    }
};