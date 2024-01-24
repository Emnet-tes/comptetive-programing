class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        box=defaultdict(int)
        cnt=0
        total=0
        box[0]=1
        for n in nums:
            total+=n
            if total%k in box.keys():
                cnt+=box[total%k]
            box[total%k]+=1
        return cnt