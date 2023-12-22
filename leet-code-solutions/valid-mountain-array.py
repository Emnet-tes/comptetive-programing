class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3  :
            return False
        else:
            index_of_maximum=arr.index(max(arr)) 
            if index_of_maximum==len(arr)-1 or index_of_maximum<=0:
                return False
            for i in range(index_of_maximum-1):
                if arr[i+1]==arr[i] or arr[i+1]<arr[i]:
                    return False
            for i in range(index_of_maximum,len(arr)-1):
                if arr[i+1]==arr[i] or arr[i+1]>arr[i]:
                    return False
        return True
