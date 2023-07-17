#User function Template for python3


class Solution():
    # Version 1: Trie + DFS
    # Let m be the length of arr[i]
    # TC: O(mn), SC: O(mn)
    def longestString(self, arr, n):
        #your code goes here
        def dfs(node, ans):
            if "_" in node:
                if len(node["_"]) > len(ans[0]):
                    ans[0] = node["_"]
                elif len(node["_"]) == len(ans[0]):
                    ans[0] = min(ans[0], node["_"])
                for k, v in node.items():
                    if k != "_":
                        dfs(v, ans)
        trie = {}
        trie["_"] = ""
        for s in arr:
            current = trie
            for c in s:
                if c not in current:
                    current[c] = {}
                current = current[c]
            current['_'] = s
        ans = [""]
        dfs(trie, ans)
        return ans[0]