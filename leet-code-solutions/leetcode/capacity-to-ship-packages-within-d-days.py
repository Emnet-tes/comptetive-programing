class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def helper(val):
            s=0
            day=0
            for i,n in enumerate(weights):
                if s+n > val:
                    day+=1
                    s=0
                s+=n
            return day+1
        

        low=max(weights)
        high=sum(weights)
        possible_day=0

        while low <= high:
            mid=(low+high)//2
            possible_day=helper(mid)

            print(possible_day)
            if possible_day<=days:
                high=mid-1
            elif possible_day>days:
                low=mid+1
        return low
        
        
