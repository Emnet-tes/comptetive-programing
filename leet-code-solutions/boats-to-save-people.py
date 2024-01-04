class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        cnt=0
        i=0
        j=len(people)-1
        while i<=j:
            if people[i]+people[j]<=limit:
                j-=1
                i+=1
            else:
                j-=1
            cnt+=1
        return cnt

        
        