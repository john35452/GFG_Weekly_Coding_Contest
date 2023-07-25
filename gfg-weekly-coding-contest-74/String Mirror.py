class Solution:
    # Version 1: Greedy
    # To get the smallest string, we would like to get the longest descending prefix.
    # However, there is a case to have consecutive same alphbet.
    # If the prefix only contains one alphbet, we only take one character.
    # For other case, we can take all of them.
    # TC: O(n), SC: O(n)
    def stringMirror(self, str : str) -> str:
        # code here
        n = len(str)
        seenGreater = False
        i = 1
        while i < n:
            if str[i] < str[i - 1]:
                seenGreater = True
            elif str[i] == str[i - 1] and seenGreater:
                seenGreater = True
            else:
                break
            i += 1
        ans = str[:i]
        return ans + ans[::-1]