class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel=set('aeiou')
        left=0
        vowelCount=0
        sub=s[:k]

        for i in range(len(sub)):
            if sub[i] in vowel:
                vowelCount+=1

        maximumVowelCount=vowelCount
        
        for right in range(k,len(s)):

            if s[left] in vowel:
                vowelCount-=1
            left+=1

            if s[right] in vowel:
                vowelCount+=1
                
            maximumVowelCount=max(vowelCount,maximumVowelCount)
        return maximumVowelCount