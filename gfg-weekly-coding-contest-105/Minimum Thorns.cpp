
class Solution {
  public:
    // Version 1: Check surrounding
    // TC: O(1), SC: O(1)
    int minimumThorns(int n, int m, vector<int> &geek, vector<int> &geekina) {
        // code here
        int dx = abs(geek[0] - geekina[0]);
        int dy = abs(geek[1] - geekina[1]);
        
        if (min(dx, dy) == 0 && max(dx, dy) == 1) 
            return -1;
            
        vector<vector<int>> point;
        point.push_back(geek);
        point.push_back(geekina);
        int direction[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        int ans[2] = {0};
        
        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < 4; j++) {
                int nx = point[i][0] + direction[j][0];
                int ny = point[i][1] + direction[j][1];
                if (1 <= nx && nx <= n && 1 <= ny && ny <= m)  {
                    ans[i] += 1;
                }
            }
        }
        
        return min(ans[0], ans[1]);
    }
};