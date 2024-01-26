class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        ans=0
        left=0
        
        number=defaultdict(int)
        for right in range(len(answerKey)):
            number[answerKey[right]]+=1

            while number['T']>k and number['F']>k :
                number[answerKey[left]]-=1
                left+=1
            ans=max(ans,right-left+1)
            
        return ans