class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        list=[]
        if num%3==0:
            d=num//3
            list.append(d-1)
            list.append(d)
            list.append(d+1)
            return list
        else:
            return list
        