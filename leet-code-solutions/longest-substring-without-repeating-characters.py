class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = ans = 0
        box= {}
        for i, right in enumerate(s):
            if box.get(right, -1) >= left:
                left = box[right] + 1
            ans= max(ans, i - left + 1)
            box[right] = i
        return ans