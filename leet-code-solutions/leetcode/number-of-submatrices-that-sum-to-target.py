class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        cnt=0
        for r in range(len(matrix)):
            for c in range(1,len(matrix[0])):
                matrix[r][c]+=matrix[r][c-1]
                
        

        for start in range(len(matrix[0])):
            for end in range(start,len(matrix[0])):
                sum=0
                box=defaultdict(int)
                box[0]=1
                
                for k in range(len(matrix)):
                    sum+=matrix[k][end]
                    if start>0:
                        sum-=matrix[k][start-1]
                    cnt+=box[sum-target]
                    box[sum]+=1
        
        return cnt