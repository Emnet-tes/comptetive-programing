class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        reveled=[]
        d=deque()
        deck.sort()
        ans=[0]*len(deck)
        for n in deck:
            d.append(n)
        
        for i in range(len(d)):
            temp=d.popleft()
            reveled.append(deck.index(temp))
            if not d:
                break
            d.append(d.popleft())
        for i,n in enumerate(reveled):
            ans[n]=deck[i]
        return ans
