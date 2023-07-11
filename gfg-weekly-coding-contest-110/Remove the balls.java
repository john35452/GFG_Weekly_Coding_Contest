

class Solution {
    // Version 1: Stack
    // TC: O(n), SC: O(n)
    public static int finLength(int N, int[] color, int[] radius) {
        // code here
        Stack<Integer> st = new Stack<Integer>();
        for (int i = 0; i < N; i++) {
            if (!st.empty() && color[st.peek()] == color[i] && radius[st.peek()] == radius[i]) {
                st.pop();
            } else {
                st.push(i);
            }
        }
        return st.size();
    }
}
        