class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans=[[1]]
        for r in range(rowIndex):
            temp=[0]+ans[-1]+[0]
            row=[]
            for c in range(len(ans[-1])+1):
                row.append(temp[c]+temp[c+1])
            ans.append(row)
        return ans[-1]