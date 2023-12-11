class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        li=Counter(nums)
        print(li.values)
        for i in li.values():
            if i>1:
                return True
        return False
        
        