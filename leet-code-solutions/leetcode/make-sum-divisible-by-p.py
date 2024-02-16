class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums) % p
        if total == 0:
            return 0

        n = len(nums)
        remainder = {0: -1}
        cur_sum = 0
        result = n
        for i, num in enumerate(nums):
            cur_sum = (cur_sum + num) % p
            target_remainder = (cur_sum - total + p) % p
            if target_remainder in remainder:
                result = min(result, i - remainder[target_remainder])
            remainder[cur_sum] = i

        return result if result < n else -1
