

//User function Template for Java

class Solution{
    // Version 1: Start with all position
    // TC: O(n), SC: O(1)
    public int[] juggling(int arr[][], int n){
        // Code Here. 
        int score[] = new int[3];
        int ball[] = new int[4];
        for (int i = 0; i < 3; i++) {
            Arrays.fill(ball, 0);
            ball[i + 1] = 1;
            for (int j = 0; j < n; j++) {
                int x = arr[j][0];
                int y = arr[j][1];
                int tmp = ball[x];
                ball[x] = ball[y];
                ball[y] = tmp;
                if (ball[arr[j][2]] > 0) score[i] += 1;
            }
        }
        int ans = 0;
        for (int i = 1; i < 3; i++) {
            if (score[i] > score[ans]) {
                ans = i;
            }
        } 
        return new int[] {ans + 1, score[ans]};
    }   

}