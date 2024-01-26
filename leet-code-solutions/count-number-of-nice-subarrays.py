class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        oddCount = 0
        res = 0
        left = 0
        count = 0
        for right in nums:
            if right % 2 == 1:
                oddCount += 1
                count = 0

            while oddCount==k:
                if nums[left] % 2 == 1:
                    oddCount -= 1
                left += 1
                count += 1
                
            res += count
        return res
                
