//User function Template for C++
class Solution{
public:
    // Version 1: Choose the minimum two dishes with different disliker
    // TC: O(nlogn), SC: O(n)
    /*
    int MinCost(int n, int prices[], int dislike[]){
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        for (int i = 0; i < n; i++) {
            pq.push({prices[i], dislike[i]});
        }
        
        int disliker = -1;
        int ans = 0;
        while (!pq.empty()) {
            pair<int, int> item = pq.top();
            pq.pop();
            if (disliker < 0) {
                disliker = item.second;
                ans += item.first;
            } else if (item.second != disliker) {
                ans += item.first;
                return ans;
            }
        }
        return -1;
    }
    */
    
    // Version 2: Store the cheapest dish dislike by disliker
    // TC: O(n), SC: O(n)
    int MinCost(int n, int prices[], int dislike[]){
        //Write Code Here
        unordered_map<int, int> dis;
        for (int i = 0; i < n; i++) {
            if (dis.find(dislike[i]) == dis.end()) {
                dis[dislike[i]] = INT_MAX;
            }
            dis[dislike[i]] = min(dis[dislike[i]], prices[i]);
        }
        
        if (dis.size() == 1) return -1;
        int one = INT_MAX, two = INT_MAX;
        for (const auto& pair: dis) {
            if (pair.second < one) {
                two = one;
                one = pair.second;
            } else if (pair.second < two) {
                two = pair.second;
            }
        }
        return one + two;
    }
};