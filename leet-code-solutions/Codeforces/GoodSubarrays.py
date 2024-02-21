from collections import defaultdict
x=int(input())
for _ in range(x):
    
    n=int(input())
    s=input()
    box=defaultdict(int)
    box[0]=1
    ans=0
    pre=0
    
    for i,v in enumerate(s):
        pre+=int(v)
        m = pre-i-1
        box[m]+=1
        ans+=box[m]-1
       
    print(ans)