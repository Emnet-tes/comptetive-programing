class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        li=[]
        for i in range(len(nums)-1):
            for j in range(nums[i]):
                if i%2==0:
                    li.append(nums[i+1])
            i+=1
        return li
