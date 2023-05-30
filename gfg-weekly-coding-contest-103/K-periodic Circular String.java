

//User function Template for Java

class Solution 
{ 
    // Version 1: Cycle
    // s[i] = s[i + K] = s[i + 2K] = .. = s[i]
    // Count the length of cycle, and check whether the frequency of character can be divided by the length.
    // Put the smaller available alphabet in the fronter group.
    // TC: O(n), SC: O(n)
    String kPeriodic(String s, int K) 
    { 
        // code here
        int[] fre = new int[26];
        for (char c: s.toCharArray()) {
            fre[c - 'a'] += 1;
        }
        
        int n = s.length();
        ArrayList<ArrayList<Integer>> group = new ArrayList<>();
        int count = 0;
        for (int i = 0; count < n; i++) {
            int j = i;
            ArrayList<Integer> g = new ArrayList<>();
            g.add(j);
            j = (j + K) % n;
            while (j != i) {
                g.add(j);
                j = (j + K) % n;
            }
            group.add(g);
            count += g.size();
        }
        
        int groupSize = group.get(0).size();
        
        for (int i = 0; i < 26; i++) {
            if (fre[i] % groupSize > 0) {
                return "-1";
            }
        }
        
        char[] res = new char[n];
        int j = 0;
        for (int i = 0; i < 26; i++) {
            while (fre[i] > 0) {
                for (int index : group.get(j)) {
                    res[index] = (char)('a' + i);
                }
                fre[i] -= groupSize;
                j += 1;
            }
        }
        return new String(res);
        
    }
}