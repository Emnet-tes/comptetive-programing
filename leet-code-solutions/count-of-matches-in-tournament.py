class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches=0
        team=0
        while n>1:
            if n%2==0:
                matches+=n/2
                team=n/2
                n=team
            else:
                matches+=(n-1)/2+1
                team=(n-1)/2
                n=team
        return int(matches)
        