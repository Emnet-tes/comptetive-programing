class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        box=defaultdict(int)
        for n in bills:
            if n==5:
                box[n]+=1
            elif n==10 and box[5]>=1:
                box[5]-=1
                box[n]+=1
            elif(n==20 and box[10]>=1 and box[5]>=1):
                box[5]-=1
                box[10]-=1
                box[20]+=1
            elif (n==20 and box[5]>=3):
                box[5]-=3
                box[20]+=1
            else:
                return False
        return True
        