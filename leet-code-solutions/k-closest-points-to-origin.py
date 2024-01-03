class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        my_dict=[]
        for i in points:
            y = (i[0]**2+i[1]**2)**0.5
            y = [i,y]
            my_dict.append(y)
        my_dict.sort(key = lambda x:x[1])
        x = my_dict[0][1]
        j = 0
        z = []
        while j<k:
            z.append(my_dict[j][0])
            j+=1
        return z