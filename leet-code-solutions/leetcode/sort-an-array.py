class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def mergesort(left,right):
            i,j=0,0
            ans=[]
            while i < len(left) or j < len(right):
                if i== len(left):
                    while j<len(right):
                        ans.append(right[j])
                        j+=1
                elif j== len(right):
                    while i<len(left):
                        ans.append(left[i])
                        i+=1
                elif left[i]<=right[j]:
                    ans.append(left[i])
                    i+=1
                else:
                    ans.append(right[j])
                    j+=1
            return ans
            
        def merge(left,right,nums):
            if left == right:
                return [nums[left]]
            mid = (left + right) // 2
            left_half = merge(left, mid, nums)
            right_half = merge(mid + 1, right, nums)
    
            return mergesort(left_half, right_half)
        left=0
        right=len(nums)-1
        return merge(left,right,nums)
        