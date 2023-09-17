#User function Template for python3

class Solution():
    # Version 1: Rule
    # TC: O(1), SC: O(1)
    def solve(self, A, B):
        #your code goes here
        if A % 2 != B % 2:
            return "Punished"
        elif A % 2 > 0:
            return "She"
        else:
            return "He"