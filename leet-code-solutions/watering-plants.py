class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        step=0
        n=capacity
        for i in range(len(plants)):
            if capacity>=plants[i] :
                step+=1
            else:
                capacity=n
                step+=2*i+1
            capacity-=plants[i]
        return step
        
        