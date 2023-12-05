class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maximum=0
        c=True
        li=[]
        for num in candies :
            maximum=max(maximum,num)
        for i in range(len(candies)):
            c=candies[i]+extraCandies >= maximum
            li.append(c)
        return li
        
        