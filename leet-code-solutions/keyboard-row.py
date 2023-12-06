class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        firstrow=set("qwertyuiop")
        secondrow=set("asdfghjkl")
        thirdrow=set("zxcvbnm")
        answer=[]
        for element in words:
            s=set(element.lower())
            if s<=firstrow or s<=secondrow or s<=thirdrow:
                answer.append(element)
        return answer
            


        