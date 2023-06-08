
class Solution {
  public:
    // Version 1: BFS
    // Start from bombs to all the matrix
    // TC: O(mn), SC: O(mn)
    vector<vector<int>> shortestDistanceFromTheBomb(vector<vector<char>> &building, int n, int m) {
        // code here
        vector<vector<int>> ans(n, vector<int>(m, -1));
        deque<pair<int, int>> q;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (building[i][j] == 'B') {
                    q.push_back({i, j});
                    ans[i][j] = 0;
                }
            }
        }
        
        vector<vector<int>> direction = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        while (!q.empty()) {
            for (int i = 0; i < q.size(); i++) {
                pair<int, int> item = q.front();
                q.pop_front();
                for (int j = 0; j < 4; j++) {
                    int nx = item.first + direction[j][0];
                    int ny = item.second + direction[j][1];
                    if (0 <= nx && nx < n && 0 <= ny && ny < m && building[nx][ny] != 'W' && ans[nx][ny] < 0) {
                        ans[nx][ny] = ans[item.first][item.second] + 1;
                        q.push_back({nx, ny});
                    }
                }
                
            }
        }
        return ans;
    }
};