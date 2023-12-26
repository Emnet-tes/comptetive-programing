class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        primary=defaultdict(int)
        secondary=defaultdict(int)
        total=0
        print(len(mat)//2)
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if r+c==len(mat)-1:
                    secondary[r+c]+=mat[r][c]
                if c-r==0:
                    primary[c-r]+=mat[r][c]
        total=primary[0]+secondary[len(mat)-1]
        if len(mat)%2==0:
            return total
        else:
            return total-mat[len(mat)//2][len(mat)//2]
        