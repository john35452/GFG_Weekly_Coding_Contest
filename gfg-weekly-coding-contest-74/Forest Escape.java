

//User function Template for Java

class Solution{
    // Version 1: BFS
    // TC: O(mn), SC: O(m + n)
    public static boolean escapeForest(int n,int m,char[][] grid)
    {
        Deque<int[]> queue = new LinkedList<int[]>();
        int[] people = new int[] {-1, -1};
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == 'X') {
                    queue.offerLast(new int[] {i, j, 0});
                } else if (grid[i][j] == 'M') {
                    people = new int[] {i, j};
                }
            }
        }
        queue.offerLast(new int[] {people[0], people[1], 1});
        
        int[][] direction = new int[][] {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        while (!queue.isEmpty()) {
            int[] item = queue.pollFirst();
            if (item[2] > 0) {
                if (item[0] == 0 || item[0] == n -1 || item[1] == 0 || item[1] == m -1) {
                    return true;
                }
            }
            for (int[] d: direction) {
                int nx = item[0] + d[0];
                int ny = item[1] + d[1];
                if (0 <= nx && nx < n && 0 <= ny && ny < m && grid[nx][ny] != 'X') {
                    if (item[2] == 0) {
                        grid[nx][ny] = 'X';
                        queue.offerLast(new int[] {nx, ny, item[2]});
                    } else if (grid[nx][ny] != 'M') {
                        grid[nx][ny] = 'M';
                        queue.offerLast(new int[] {nx, ny, item[2]});
                    }
                }
            }
        }
        return false;
    }
}