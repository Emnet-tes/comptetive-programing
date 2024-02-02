class Solution:
    def minimumSteps(self, s: str) -> int:
        ans = 0
        cnt = 0
        for c in reversed(s):
            if c == '0':
                cnt += 1
            else:
                ans += cnt
            
        return ans