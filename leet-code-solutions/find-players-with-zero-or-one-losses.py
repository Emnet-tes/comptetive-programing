class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winner=[]
        loser=[]
        for i in range(len(matches)):
            winner.append(matches[i][0])
            loser.append(matches[i][1])
        c=Counter(loser)
        l=[]
        m=[]
        for i in range(len(winner)):
            if c[winner[i]]==0:
                l.append(winner[i])
            if c[winner[i]]==1:
                m.append(winner[i])
            if c[loser[i]]==1:
                m.append(loser[i])
        
        l=list(set(l))
        m=list(set(m))
        l.sort()
        m.sort()

        return [l,m]

        