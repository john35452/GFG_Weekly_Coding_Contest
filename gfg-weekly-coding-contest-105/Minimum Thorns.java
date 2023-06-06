

class Solution{
    // Version 1: Check surrounding
    // TC: O(1), SC: O(1)
    public int minimumThorns(int n, int m, int geek[], int geekina[]){
        // Code Here.
        int dx = Math.abs(geek[0] - geekina[0]);
        int dy = Math.abs(geek[1] - geekina[1]);
        if (Math.max(dx, dy) == 1 && Math.min(dx, dy) == 0)
            return -1;
            
        int points[][] = new int[][] {geek, geekina};
        int ans[] = new int[2];
        int direction[][] = new int[][] {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        
        
        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < 4; j++) {
                int nx = points[i][0] + direction[j][0];
                int ny = points[i][1] + direction[j][1];
                if (1 <= nx && nx <= n && 1 <= ny && ny <= m)
                    ans[i] += 1;
            }
        }
        return Math.min(ans[0], ans[1]);
    }
}