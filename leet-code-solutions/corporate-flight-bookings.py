class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        result=[0]*(n+1)
        for i,j,k in bookings:
            result[i-1]+=k
            result[j]-=k
        ans=[]
        total=0
        
        for i in range(len(result)-1):
            total += result[i]
            ans.append(total)
        return ans