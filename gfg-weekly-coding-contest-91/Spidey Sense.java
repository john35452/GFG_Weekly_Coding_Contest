

class Solution{
    // Version 1: BFS
    // Start from bombs to all the matrix
    // TC: O(mn), SC: O(mn)
    public int[][] shortestDistanceFromTheBomb(char building[][], int n, int m){
        // Code Here. 
        int ans[][] = new int[n][m];
        for (int i = 0; i < n; i++) {
            Arrays.fill(ans[i], -1);
        }
        
        Deque<int[]> deque = new ArrayDeque<int[]>();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (building[i][j] == 'B') {
                    deque.offerLast(new int[] {i, j});
                    ans[i][j] = 0;
                }
            }
        }
        
        int direction[][] = new int[][] {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        int step = 0;
        while (!deque.isEmpty()) {
            int size = deque.size();
            for (int i = 0; i < size; i++) {
                int[] item = deque.pollFirst();
                for (int j = 0; j < 4; j++) {
                    int nx = item[0] + direction[j][0];
                    int ny = item[1] + direction[j][1];
                    if (0 <= nx && nx < n && 0 <= ny && ny < m && ans[nx][ny] < 0 && building[nx][ny] != 'W' && ans[nx][ny] < 0) {
                        ans[nx][ny] = ans[item[0]][item[1]] + 1;
                        deque.offerLast(new int[] {nx, ny});
                    }
                }
            }
        }
        return ans;
    }
    
}