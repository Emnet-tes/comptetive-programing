class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        box=defaultdict(int)
        for i in range(len(arr2)):
            box[arr2[i]]=i
        y=sorted(arr1,key=lambda  x : box[x])
        li=[]
        for j in range(len(arr1)):
            if arr1[j] not in arr2:
                y.remove(arr1[j])
                li.append(arr1[j])
        li.sort()
        for i in range(len(li)):
            y.append(li[i])
        return y
        