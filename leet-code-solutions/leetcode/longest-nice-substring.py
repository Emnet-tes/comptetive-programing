class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def dfs(substring):
            box = set(substring)
            if len(substring) < 2:
                return ''
            for i,n in enumerate(substring):
                if not (n.lower() in box and n.upper() in box):
                    left = dfs(substring[:i])
                    right = dfs(substring[i+1:])
                    
                    if len(left) >= len(right):
                        return left
                    else:
                        return right
            return substring
        return dfs(s)