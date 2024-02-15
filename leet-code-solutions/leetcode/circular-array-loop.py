class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        checked=set()
        n=len(nums)
        for i in range(n):
            if i not in checked:
                loop=set()
                while True:
                    if i in loop:
                        return True
                    checked.add(i)
                    loop.add(i)
                    prev,i=i,(i+nums[i])%n
                    if prev==i:
                        break
                    if nums[prev]>0 != nums[i]<0:
                        break
        return  False

        