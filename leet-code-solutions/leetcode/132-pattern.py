class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        maxi = float('-inf')
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < maxi:
                return True
            while stack and stack[-1] < nums[i]:
                maxi = stack[-1]
                stack.pop()
            stack.append(nums[i])
        return False