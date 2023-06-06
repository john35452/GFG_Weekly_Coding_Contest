

//User function Template for Java

class Solution{
    // Version 1: Make the number of numbers mod 1 and mod 2 to be equal
    // TC: O(n), SC: O(1)
    /*
    public int minimumOperations(int n, int a[]){
        // Code Here. 
        int fre[] = new int[3];
        for (int v: a) {
            fre[v % 3] += 1;
        }
        
        if ((fre[1] + 2 * fre[2]) % 3 > 0) return -1;
        
        int ans = 0;
        while (fre[1] != fre[2]) {
            if (fre[1] > fre[2]) {
                fre[1] -= 2;
                fre[2] += 1;
            } else {
                fre[2] -= 2;
                fre[1] += 1;
            }
            ans += 1;
        }
        return ans + fre[1];
    }
    */
    
    // Version 2: Greedy
    // We can match all mod 1 and mod 2 first, then for the remaining part.
    // We can combine every 3 of them.
    // TC: O(n), SC: O(1)
    public int minimumOperations(int n, int a[]){
        // Code Here. 
        int fre[] = new int[3];
        for (int v: a) {
            fre[v % 3] += 1;
        }
        
        int diff = Math.min(fre[1], fre[2]);
        int ans = diff;
        fre[1] -= diff;
        fre[2] -= diff;
        if (fre[1] % 3 != 0 || fre[2] % 3 != 0) return -1;
        return ans + 2 * (fre[1] / 3 + fre[2] / 3);
    }
    
}