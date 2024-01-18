class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        box = defaultdict(int)
        left = 0
        ans = 0

        for right in range(len(fruits)):
            box[fruits[right]] += 1

            while len(box) > 2:
                box[fruits[left]] -= 1
                if box[fruits[left]] == 0:
                    del box[fruits[left]]
                left += 1
            
            ans = max(ans, right - left + 1)

        return ans