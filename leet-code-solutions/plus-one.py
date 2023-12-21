class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=len(digits)
        x=''
        for i in range(n):
            x+=str(digits[i])
        y=str(int(x)+1)
        digit=[]
        for i in range(len(y)):
            digit.append(int(y[i]))
        return digit
        
        
        
