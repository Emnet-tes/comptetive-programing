class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        n1=len(list1)
        n2=len(list2)
        li={}
        mylist=[]
        maximum=max(n2,n1)
        ans=float('inf')
        for i in range(n1) :
            if list1[i] in list2 :
                j=list2.index(list1[i])
                index=i+j
                li.update({list1[i]: index})
            
        minimum=min(li.values())
        for i,val in li.items():
            if val==minimum:
                mylist.append(i)

        return mylist
