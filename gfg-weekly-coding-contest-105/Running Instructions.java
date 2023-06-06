

class Solution{
    // Version 1: BFS
    // TC: O(nm), SC: O(m)
    /*
    public String instructionCheck(int m, int n, int k[]){
        // Code Here.
        Set<Integer> current = new HashSet<>();
        Set<Integer> nextStep = new HashSet<>();
        current.add(k[0]);
        for (int i = 1; i < k.length; i++) {
            Iterator<Integer> iter = current.iterator();
            while (iter.hasNext()) {
                int val = iter.next();
                nextStep.add((val + k[i]) % m);
                nextStep.add((val - k[i]) % m);
                iter.remove();
            }
            Set<Integer> tmp = current;
            current = nextStep;
            nextStep = tmp;
        }
        if (current.contains(0)) {
            return "YES";
        } else {
            return "NO";
        }
    }
    */
    
    // Version 2: DP
    // dp[i][val]: The result starting from index i and score val.
    // TC: O(nm) SC: O(nm)
    public String instructionCheck(int m, int n, int k[]){
        // Code Here.
        Boolean dp[][] = new Boolean[k.length][m + 1];
        if (run(0, 0, m, dp, k)) {
            return "YES";
        } else {
            return "NO";
        }
    }
    
    boolean run(int index, int score, int m, Boolean[][] dp, int k[]) {
        if (index == k.length) {
            if (score == 0) return true;
            else return false;
        } else if (dp[index][score] == null) {
            dp[index][score] = 
                run(index + 1, (score + k[index] % m + m) % m, m, dp, k) |
                run(index + 1, (score - k[index] % m + m) % m, m, dp, k);
        }
        return dp[index][score];
    }
}