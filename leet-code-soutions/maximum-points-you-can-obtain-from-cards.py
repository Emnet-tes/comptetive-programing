class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total=sum(cardPoints)
        current=sum(cardPoints[:len(cardPoints)-k])
        ans=current

        for right in range(len(cardPoints)-k,len(cardPoints)):
            current += cardPoints[right]
            current -= cardPoints[right-len(cardPoints)+k]
            ans = min(ans,current)
        return total-ans
