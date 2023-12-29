class Solution:
    def smallestNumber(self, num: int) -> int:
        numberbox=str(num)
        number=[]
        for i in range(len(numberbox)):
            number.append(numberbox[i])
        if number[0] == '-':
            for i in range(1,len(number)-1):
                index=i
                for j in range(i+1,len(number)):
                    if number[j]>number[index]:
                        index=j
                if index!=i:
                    number[index],number[i]=number[i],number[index]
        else:
            number.sort()
            for i in range(1,len(number)):
                if int(number[i])>0 and int(number[0])==0:
                   number[0],number[i]=number[i],number[0]
            
            
        ans= "".join(number)
        print(ans)    
        return int(ans)
            