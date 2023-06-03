#User function Template for python3

class Solution:
    # Version 1: Count
    # TC: O(n), SC: O(1)
    def valuableString(self, n, arr):
        # code here
        vowels = "aeiou"
        ans_index = -1
        ans_val = -1
        for i, s in enumerate(arr):
            balance = 0
            for c in s:
                if c in vowels:
                    balance += 1
                else:
                    balance -= 1
            if abs(balance) > ans_val:
                ans_val = abs(balance)
                ans_index = i
        return arr[ans_index]
        