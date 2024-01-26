class Solution:
    def balancedString(self, s: str) -> int:
        size = len(s)
        balance = size // 4
        box = Counter(s)

        left = 0
        cnt = float('inf')
        for right in range(size):
            box[s[right]] -= 1
            while all(val <= balance for val in box.values()) and left<size:
                cnt = min(cnt, right - left + 1)
                box[s[left]] += 1
                left += 1

        return 0 if cnt == float('inf') else cnt