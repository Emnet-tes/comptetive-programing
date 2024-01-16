class NumArray:

    def __init__(self, nums: List[int]):
        self.nums=nums
        self.total=[0]
        self.t=0
        for i in range(len(self.nums)):
            self.t+=self.nums[i]
            self.total.append(self.t)
        print(self.total)

    def sumRange(self, left: int, right: int) -> int:
        return self.total[right+1]-self.total[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)