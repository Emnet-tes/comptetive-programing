class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d=defaultdict(int)
        for i,n in enumerate(nums2):
            d[n]=i
        ans=[]
        
        for i,n in enumerate(nums1):
            j=1
            while d[n]+j<len(nums2):
                if nums2[d[n]+j]>n:
                    ans.append(nums2[d[n]+j])
                    break
                j+=1
            if j+d[n]>=len(nums2):
                ans.append(-1)
        return ans




