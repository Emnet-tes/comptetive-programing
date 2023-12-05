class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        sword1="".join(word1)
        sword2="".join(word2)
        return  sword2 == sword1
        
        