//User function Template for Java

class Solution{
    // Version 1: Check the surrounding of terrorist
    // TC: O(mn), SC: O(mn)
    public boolean saveCivilians(int n, int m, char grid[][]){
        // Code your solution here.
        int direction[][] = new int[][] {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == 'T') {
                    for (int k = 0; k < 4; k++) {
                        int nx = i + direction[k][0];
                        int ny = j + direction[k][1];
                        if (0 <= nx && nx < n && 0 <= ny && ny < m) {
                            if (grid[nx][ny] == 'C') {
                                return false;
                            }
                        }
                    }
                }
            }
        }
        return true;
    }
}
