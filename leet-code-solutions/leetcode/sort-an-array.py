class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(low, mid, high):
            res = [0] * (high - low + 1)
            i,j,k=low,mid+1,0
            while i < mid+1 or j < high+1:
                if j > high or (i< mid+1 and nums[i]<nums[j]):
                    res[k]=nums[i]
                    i+=1
                    k+=1
                else:
                    res[k]=nums[j]
                    j+=1
                    k+=1
            nums[low:high+1]=res
        def mergeSort(low, high):
            if low < high:
                mid = low + (high - low) // 2
                mergeSort(low, mid)
                mergeSort(mid + 1, high)
                merge(low, mid, high)
        mergeSort(0, len(nums) - 1)
        return nums
