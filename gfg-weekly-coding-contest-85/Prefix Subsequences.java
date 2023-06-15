

//User function Template for Java

class Solution{
    // Version 1: Check the longest prefix in t
    // TC: O(m), SC: O(1)
    static int maximumPrefix(int n, int m, String s, String t){
        int i = 0;
        for (int j = 0; j < m; j++) {
            if (i < n && s.charAt(i) == t.charAt(j)) {
                i++;
            }
        }
        return i == n? -1: i + 1;
    }
}