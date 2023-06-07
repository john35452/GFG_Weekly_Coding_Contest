

//User function Template for Java

class Solution{
    // Version 1: BFS
    // Starts with fires first, then the person
    // TC: O(mn), SC: O(mn)
    public int avoidFire(int n, int m, int a[][], int x, int y){
        // Code Here.
        if (x == n - 1 && y == m - 1) return 1;
        Deque<int[]> deque = new ArrayDeque<>();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (a[i][j] > 0) {
                    deque.offerLast(new int[] {i, j, 1});
                }
            } 
        }
        deque.offerLast(new int[] {x, y, 0});
        
        int direction[][] = new int[][] {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        while (!deque.isEmpty()) {
            int size = deque.size();
            for (int i = 0; i < size; i++) {
                int[] item = deque.pollFirst();
                if (item[0] == n - 1 && item[1] == m - 1) {
                    if (item[2] == 0) return 1;
                    else return 0;
                }
                for (int j = 0; j < 4; j++) {
                    int nx = item[0] + direction[j][0];
                    int ny = item[1] + direction[j][1];
                    if (0 <= nx && nx < n && 0 <= ny && ny < m && a[nx][ny] != 1) {
                        if (item[2] > 0) {
                            a[nx][ny] = 1;    
                        }
                        deque.offerLast(new int[] {nx, ny, item[2]});
                    }
                }
            } 
        }
        return 0;
    }
}
