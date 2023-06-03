

//User function Template for Java

class Solution 
{ 
    
    // Version 1: Greedy
    // Remove the all bigger pattern first, then the smaller one.
    // TC: O(n), SC: O(n)
    static long solve(int X,int Y, String S)
	{    
	    // code here
        int n = S.length();
        String[] p = new String[] {"pr", "rp"};
        if (Y > X) {
            String tmp = p[1];
            p[1] = p[0];
            p[0] = tmp;
            int tmp2 = Y;
            Y = X;
            X = tmp2;
        }
        
        long ans = 0;
        ArrayList<Character> stack = new ArrayList<Character>();
        for (char c: S.toCharArray()) {
            stack.add(c);
            while (stack.size() > 1) {
                if (stack.get(stack.size() - 2) == p[0].charAt(0) && stack.get(stack.size() - 1) == p[0].charAt(1)) {
                    ans += X;
                    stack.remove(stack.size() - 1);
                    stack.remove(stack.size() - 1);
                } else {
                    break;
                }
            }
        }
        
        ArrayList<Character> stack2 = new ArrayList<Character>();
        for (char c: stack) {
            stack2.add(c);
            while (stack2.size() > 1) {
                if (stack2.get(stack2.size() - 2) == p[1].charAt(0) && stack2.get(stack2.size() - 1) == p[1].charAt(1)) {
                    ans += Y;
                    stack2.remove(stack2.size() - 1);
                    stack2.remove(stack2.size() - 1);
                } else {
                    break;
                }
            }
        }
        return ans;
	}
	
} 