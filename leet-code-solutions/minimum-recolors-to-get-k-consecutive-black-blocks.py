class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left=0
        firstCount=Counter(blocks[:k])
        minimumBlack=firstCount['W']
        for right in range(k,len(blocks)):
            firstCount[blocks[right]]+=1
            firstCount[blocks[left]]-=1
            left+=1
            minimumBlack=min(minimumBlack,firstCount['W'])
        print(left)
        return minimumBlack