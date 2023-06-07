class Solution {
  public:
    
    // Version 1: BFS
    // Starts with fires first, then the person
    // TC: O(mn), SC: O(mn)
    bool avoidFire(int n, int m, int x, int y, vector<vector<int>> &arr) {
        // code here
        if (x == n - 1 && y == m - 1) return true;
        queue<vector<int>> queue;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (arr[i][j] > 0) {
                    queue.push(vector<int>{{i, j, 1}});
                }
            }
        }
        queue.push(vector<int>{{x, y, 0}});
        int direction[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        
        while (!queue.empty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                vector<int> item = queue.front();
                queue.pop();
                if (item[0] == n - 1 && item[1] == m - 1) {
                    return item[2] == 0;
                }
                for (int j = 0; j < 4; j++) {
                    int nx = item[0] + direction[j][0];
                    int ny = item[1] + direction[j][1];
                    if (0 <= nx && nx < n && 0 <= ny && ny < m && arr[nx][ny] == 0) {
                        if (item[2] > 0) {
                            arr[nx][ny] = 1;
                        }
                        queue.push(vector<int>{{nx, ny, item[2]}});
                    }
                } 
            }
        }
        return false;
        
    }
};