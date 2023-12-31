class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        sortedCosts=sorted(costs)
        sumOfCosts=0
        buy=0
        for num in sortedCosts:
            sumOfCosts+=num
            if sumOfCosts<=coins:
                buy+=1
            else:
                break
        return buy

        