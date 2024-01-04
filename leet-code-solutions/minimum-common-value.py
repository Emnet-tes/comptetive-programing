class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        f=0
        s=0
        minimum=10**9
        if not set(nums1)&set(nums2) :
            return -1
        while f<len(nums1) and s<len(nums2):
            if nums1[f]<nums2[s]:
                f+=1
            elif nums1[f]>nums2[s]:
                s+=1
            else:
                minimum=min(minimum,nums1[f])
                f+=1
                s+=1
        return minimum


