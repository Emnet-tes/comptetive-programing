class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        cardsOccurrence=defaultdict(int)
        left=0
        minimumSize=float('inf')
        for right in range(len(cards)):
            cardsOccurrence[cards[right]]+=1
            while cardsOccurrence[cards[right]]>1:
                minimumSize=min(minimumSize,right-left+1)
                cardsOccurrence[cards[left]]-=1
                left+=1
        if minimumSize!=float('inf'):
            return(minimumSize )
        else :
              return(-1)