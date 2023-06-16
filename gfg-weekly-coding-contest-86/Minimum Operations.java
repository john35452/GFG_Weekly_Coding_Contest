


//User function Template for Java

class Solution{
    // Version 1: Greedy
    // Store the position of maximum value
    // Consider the number non-maximum value in front of a maximum value.
    // Even: It takes count / 2 to update them.
    // x x x x 5 =>     5 5 5
    //              5 5 5
    // Odd: It taks (count + 1) / 2 to update them
    // and one number after the maximum number will be updated as well.
    // x x x 5 y => 5 5 5
    //                  5 5 5
    // Therefore, we can increase answer by (count + 1) / 2 to update non-maximum numbers.
    // We only need to take care the non-maximum numbers after the last maxium number afterward.
    // TC: O(n), SC: O(n)
    public int minimumOperations(int n, int a[]){
        // Code Here.
        int maxv = Integer.MIN_VALUE;
        for (int val: a) {
            maxv = Math.max(maxv, val);
        }
         
        ArrayList<Integer> pos = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            if (a[i] == maxv) pos.add(i);
        }
        
        int l = 0, i = 0, ans = 0, count;
        for (int j = 0; j < pos.size(); j++) {
            i = pos.get(j);
            count = i - l;
            ans += (count + 1) /2;
            if (count % 2 > 0) {
                l = i + 2;
            } else {
                l = i + 1;
            }    
        }
        
        count = n - l;
        ans += (count + 1) / 2;
        return ans;
    }
}