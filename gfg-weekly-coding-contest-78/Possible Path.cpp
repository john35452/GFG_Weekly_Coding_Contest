
class Solution {
  public:
    // Version 1: BFS
    // TC: O(mn), SC: O(mn)
    int possiblePath(int n, int m, vector<vector<int>> &grid) {
        // code here
        vector<vector<bool>> visited(n, vector<bool>(m, false));
        deque<pair<int, int>> queue;
        queue.push_back({0, 0});
        visited[0][0] = true;
        int direction[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        int ans = 0;
        while (!queue.empty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                auto item = queue.front();
                queue.pop_front();
                int x = item.first;
                int y = item.second;
                if (x == n - 1 && y == m - 1) return ans;
                bool power = grid[x][y] == 2;
                for (const auto& d : direction) {
                    int nx = x + d[0];
                    int ny = y + d[1];
                    if (0 <= nx && nx < n && 0 <= ny && ny < m && !visited[nx][ny]) {
                        if (grid[nx][ny] == 1) {
                            if (power) {
                                visited[nx][ny] = true;
                                queue.push_back({nx, ny});
                            }
                        } else {
                            visited[nx][ny] = true;
                            queue.push_back({nx, ny});
                        }
                    }
                } 
            }
            ans++;
        }
        return -1;
    }
};