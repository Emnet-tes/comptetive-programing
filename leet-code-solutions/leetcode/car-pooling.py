class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        ans=[0 for _ in range(1001)]
        maxi=0
        for i,j,k in trips:
            maxi=max(maxi,k)
            ans[j]+=i
            ans[k]-=i
        
        pre=0
        for n in range(1001):
            
            if pre>capacity:
                return False
            pre+=ans[n]
        return True